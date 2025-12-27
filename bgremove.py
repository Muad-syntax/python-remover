import os
from withoutbg import WithoutBG

folder_masuk = "input_foto"
folder_keluar = "hasil_foto"

os.makedirs(folder_keluar, exist_ok=True)

print("Sedang membuat model AI... Mohon tunggu sebentar.")
remove = WithoutBG.opensource()

files = os.listdir(folder_masuk)
print(f"Ditemukan {len(files)} file. Mulai memproses...")

for filename in files:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            input_path = os.path.join(folder_masuk, filename)
            bgkucing = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(folder_keluar, bgkucing)

            print(f"Sedang memproses: {filename} ...")

            result = remove.remove_background(input_path)
            result.save(output_path)

            print(f"Berhasil! Disimpan di: {output_path}")
        except Exception as e:
            print(f"Gagal memproses {filename}. Error: {e}")

print("--- SELESAI SEMUA! ---")