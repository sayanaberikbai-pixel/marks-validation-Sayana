import pandas as pd
import numpy as np


df = pd.read_csv("marks.csv")
df["points_num"] = pd.to_numeric(df["points"], errors="coerce")


df["ok"] = df["points_num"].notna() & df["points_num"].between(0, 100)


print(" ok бағанасы бар толық DataFrame")
print(df[["id", "name", "points", "ok"]].to_string(index=True))


print("Алғашқы 10 БҰЗУШЫЛЫҚ (ok == False)")

violations = df[df["ok"] == False].head(10)
print(violations[["id", "name", "points", "ok"]].to_string(index=True))
print(f"\nБарлық бұзушылық саны: {(df['ok'] == False).sum()}")
