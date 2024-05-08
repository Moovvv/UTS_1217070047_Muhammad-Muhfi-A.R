import cv2

# Membaca gambar
gambar = cv2.imread('muhfi.jpeg')

# Mendapatkan tipe data gambar
tipe_data = gambar.dtype

# Menampilkan tipe data gambar
print(f"Tipe data gambar: {tipe_data}")
