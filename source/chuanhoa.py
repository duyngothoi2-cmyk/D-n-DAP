import pandas as pd
import numpy as np
import re

df = pd.read_csv("D:\\Hoc\\DAP\\D-n-DAP\\data\\raw\\batdongsan_hcm.csv")

print("Kích thước ban đầu:", df.shape)

df = df.drop_duplicates(subset="ma_tin")

text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .replace("nan", np.nan)
    )

def convert_price(value):
    if pd.isna(value):
        return np.nan

    value = str(value).lower().strip()
    value = value.replace(",", ".")

    if "tỷ" in value:
        match = re.search(r"([\d.]+)", value)
        if match:
            return float(match.group(1))

    if "triệu" in value:
        match = re.search(r"([\d.]+)", value)
        if match:
            return float(match.group(1)) / 1000

    return np.nan


df["gia_ty"] = df["gia"].apply(convert_price)

def convert_area(value):
    if pd.isna(value):
        return np.nan

    value = str(value).lower().strip()
    value = value.replace(",", ".")

    match = re.search(r"([\d.]+)", value)

    if match:
        return float(match.group(1))

    return np.nan


df["dien_tich_m2"] = df["dien_tich"].apply(convert_area)

df["so_phong_ngu"] = pd.to_numeric(
    df["so_phong_ngu"],
    errors="coerce"
)

df["so_tang"] = pd.to_numeric(
    df["so_tang"],
    errors="coerce"
)

df["so_phong"] = pd.to_numeric(
    df["so_phong"],
    errors="coerce"
)

df["ngay_dang"] = pd.to_datetime(
    df["ngay_dang"],
    errors="coerce",
    dayfirst=True
)

df["tinh_thanh"] = df["tinh_thanh"].fillna("Hồ Chí Minh")

df.loc[df["gia_ty"] <= 0, "gia_ty"] = np.nan
df.loc[df["dien_tich_m2"] <= 0, "dien_tich_m2"] = np.nan
df.loc[df["so_phong_ngu"] < 0, "so_phong_ngu"] = np.nan

df["gia_tren_m2"] = (
    df["gia_ty"] * 1000 / df["dien_tich_m2"]
)


df = df.dropna(
    subset=["gia_ty", "dien_tich_m2"]
)

df = df[
    (df["gia_ty"] > 0) &
    (df["dien_tich_m2"] > 10) &
    (df["dien_tich_m2"] < 1000)
]

df = df.reset_index(drop=True)

df.to_csv(
    "D:\\Hoc\\DAP\\D-n-DAP\\data\\clean\\batdongsan_hcm_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Kích thước sau khi chuẩn hóa:", df.shape)

print("\nCác cột dữ liệu:")
print(df.columns.tolist())

print("\n5 dòng đầu:")
print(df.head())