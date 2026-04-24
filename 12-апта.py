import pandas as pd

df = pd.read_csv("marks.csv")
df["points_num"] = pd.to_numeric(df["points"], errors="coerce")
df["ok"] = df["points_num"].notna() & df["points_num"].between(0, 100)


df_clean = (
    df[df["ok"]]
    .drop(columns=["points_num", "ok"])
    .reset_index(drop=True)
)

output_path = "marks_clean.csv"
df_clean.to_csv(output_path, index=False)


print(" — marks_clean.csv сақтау")
print(f"Бастапқы жолдар  : {len(df)}")
print(f"Жарамды жолдар   : {len(df_clean)}")
print(f"Алынып тасталды  : {len(df) - len(df_clean)}")
print(f"Файл сақталды    : {output_path}\n")
print(df_clean.to_string(index=False))