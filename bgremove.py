import os
from withoutbg import WithoutBG

# konfigurasi folder
folder_masuk = "input_foto"
folder_keluar = "hasil_foto"

# buat folder output jika belum ada
os.makedirs(folder_keluar, exist_ok=True)

# siapkan model AI-nya
print("Sedang membuat model AI... Mohon tunggu sebentar.")
remove = WithoutBG.opensource()

# anbil daftar semua file di folder masuk
files = os.listdir(folder_masuk)
print(f"Ditemukan {len(files)} file. Mulai memproses...")

# looping untuk memproses setiap gambar
for filename in files:
    # cek, apakah file gambar adalah gambar (jpg, jpeg, atau png)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            input_path = os.path.join(folder_masuk, filename)

            # ganti ekstensi file jadi .png untuk output (karena bg transparan butuh PNG)
            bgkucing = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(folder_keluar, bgkucing)

            print(f"Sedang memproses: {filename} ...")

            # proses penghapusan background
            # menggunakan methode dari library withoutbg
            result = remove.remove_background(input_path)
            result.save(output_path)

            print(f"Berhasil! Disimpan di: {output_path}")
        except Exception as e:
            print(f"Gagal memproses {filename}. Error: {e}")

print("--- SELESAI SEMUA! ---")