import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import io
import sys
from flask import Flask, request, jsonify

CSV_PATH = "marks.csv"


df = pd.read_csv(CSV_PATH)
points_raw = pd.to_numeric(df["points"], errors="coerce").values

mask_nan       = np.isnan(points_raw)
mask_below_zero = (~mask_nan) & (points_raw < 0)
mask_above_100  = (~mask_nan) & (points_raw > 100)
mask_invalid    = mask_nan | mask_below_zero | mask_above_100

idx_nan   = np.where(mask_nan)[0]
idx_below = np.where(mask_below_zero)[0]
idx_above = np.where(mask_above_100)[0]
idx_bad   = np.where(mask_invalid)[0]

print("=" * 50)
print(f"Жалпы жазба саны     : {len(points_raw)}")
print(f"NaN индекстері       : {idx_nan.tolist()}")
print(f"0-ден кіші индекстер : {idx_below.tolist()}")
print(f"100-ден үлкен индекс : {idx_above.tolist()}")
print(f"Барлық қате индекстер: {idx_bad.tolist()}")


n_bad  = int(np.sum(mask_invalid))
n_good = int(np.sum(~mask_invalid))
print("=" * 50)
print(f"Хороших строк: {n_good}")
print(f"Плохих строк : {n_bad}")


df["points_num"] = points_raw
df["ok"] = ~mask_invalid
violations = df[~df["ok"]].head(10)
print("=" * 50)
print("Первые 10 нарушений:")
print(violations[["points", "ok"]].to_string())


df[df["ok"]][["points"]].to_csv("marks_clean.csv", index=False)
print("=" * 50)
print("Сохранено: marks_clean.csv")


fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(["Валидные", "Невалидные"], [n_good, n_bad],
              color=["#4CAF50", "#F44336"], width=0.5)
for bar, val in zip(bars, [n_good, n_bad]):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.2, str(val),
            ha="center", fontsize=13, fontweight="bold")
ax.set_title("Проверка баллов 0–100")
ax.set_ylabel("Количество строк")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("marks_bar.png", dpi=150)
plt.close()
print("Сохранено: marks_bar.png")


def build_app():
    app = Flask(__name__)

    @app.route("/validate", methods=["POST"])
    def validate_csv():
        if "file" not in request.files:
            return jsonify({"error": "Нет файла"}), 400
        try:
            data = pd.read_csv(io.BytesIO(request.files["file"].read()))
            nums = pd.to_numeric(data["points"], errors="coerce")
            ok   = nums.notna() & (nums >= 0) & (nums <= 100)
            bad  = data.index[~ok].tolist()
            return jsonify({
                "valid_count"     : int(ok.sum()),
                "invalid_count"   : int((~ok).sum()),
                "first_20_errors" : bad[:20]
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 422

    return app

if "--serve" in sys.argv:
    print("Сервер запущен: http://localhost:5000/validate")
    build_app().run(debug=False, port=5000)
else:
    print("=" * 50)
    print("Flask іске қосу үшін:")
    print("  python 14-апта.py --serve")
