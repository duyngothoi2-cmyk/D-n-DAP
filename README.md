# Thu thap du lieu bat dong san TP. Ho Chi Minh

Du an thu thap du lieu bat dong san phuc vu hoc tap. Nguon dang duoc xu ly trong giai doan hien tai la **NhaTot (Cho Tot)**. Batdongsan.com.vn duoc tam hoan vi request tu dong dang tra HTTP 403.

## Cau truc thu muc

```text
.
|-- data/
|   |-- external/       # Du lieu tu nguon hop le ben ngoai, khong commit mac dinh
|   |-- processed/      # Du lieu sau xu ly
|   `-- raw/            # Checkpoint va du lieu tho
|-- logs/               # Log chay crawler
|-- notebooks/          # Notebook phan tich ve sau
|-- source/
|   `-- thu_thap_data_du_phong.ipynb
|-- test/               # Kiem tra nho cho parser/helper
`-- tham_khao/          # Tai lieu tham khao cua nhom
```

## Cai dat

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Chay NhaTot

Mo `source/thu_thap_data_du_phong.ipynb` va chay theo thu tu:

1. Cell 2: import va tao thu muc.
2. Cell 3: nap ham parser, checkpoint va crawler NhaTot.
3. Cell 4: nap parser Batdongsan offline, khong gui request.
4. Cell 6: chay NhaTot. Crawler doc `data/raw/nhatot_raw.csv` va tiep tuc tu checkpoint.
5. Cell 7: giu Batdongsan tam hoan.
6. Cell 8: kiem tra so dong, ID/URL trung va file raw.

NhaTot dung endpoint JSON cong khai, phan trang bang tham so `o`, va khong dung bo loc `st='s,k'` vi bo loc nay chi tra 521 tin. Checkpoint duoc ghi sau moi 150 dong.

## Batdongsan tam hoan

Khong tu dong request Batdongsan. Parser offline chi doc cac response HTML da duoc luu hop le trong `data/raw/batdongsan_pages/*.html`. Khong su dung CAPTCHA, cookie phien, token ca nhan, proxy, fingerprint hay ky thuat vuot 403.

De bat dau lai phan nay can API, file export, hoac quyen truy cap/crawler chinh thuc. Khong dua du lieu gia vao dataset.

## GitHub

Truoc khi push, kiem tra:

```powershell
git status
git diff --stat
git add README.md requirements.txt .gitignore source data logs test tham_khao
git commit -m "Organize data collection notebook"
git push
```

File raw, response HTML va log rieng khong duoc commit theo `.gitignore`.
