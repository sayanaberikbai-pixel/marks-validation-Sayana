import numpy as np
import pandas as pd


df = pd.read_csv("marks.csv")
points_raw = pd.to_numeric(df["points"], errors="coerce").values


mask_nan = np.isnan(points_raw)
mask_invalid = mask_nan | (~mask_nan & ((points_raw < 0) | (points_raw > 100)))
mask_valid = ~mask_invalid


good_count = int(np.sum(mask_valid))
bad_count = int(np.sum(mask_invalid))

print("=" * 50)
print("=" * 50)
print(f" Жарамды  (good): {good_count}")
print(f" Жарамсыз (bad) : {bad_count}")
print(f"Барлығы        : {good_count + bad_count}")
print(f"Валидтілік      : {good_count / (good_count + bad_count) * 100:.1f}%")