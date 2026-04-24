import numpy as np
import pandas as pd


df = pd.read_csv("marks.csv")
points_raw = pd.to_numeric(df["points"], errors="coerce").values  # float64 NumPy array

print("=" * 50)
print("=" * 50)
print(f"Жалпы жазба саны: {len(points_raw)}")
print(f"Массив (алғашқы 10): {points_raw[:10]}\n")


mask_nan = np.isnan(points_raw)  # NaN болса True
mask_below_zero = (~mask_nan) & (points_raw < 0)  # 0-ден кіші
mask_above_100 = (~mask_nan) & (points_raw > 100)  # 100-ден үлкен
mask_invalid = mask_nan | mask_below_zero | mask_above_100  # кез-келген қате


idx_nan = np.where(mask_nan)[0]
idx_below = np.where(mask_below_zero)[0]
idx_above = np.where(mask_above_100)[0]
idx_bad = np.where(mask_invalid)[0]

print(f"NaN индекстері       : {idx_nan.tolist()}")
print(f"0-ден кіші индекстер : {idx_below.tolist()}")
print(f"100-ден үлкен индекс : {idx_above.tolist()}")
print(f"Барлық қате индекстер: {idx_bad.tolist()}")
