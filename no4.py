import cv2

# Membaca gambar
gambar = cv2.imread('muhfi.jpeg')

# Mendapatkan dimensi gambar (tinggi, lebar)
tinggi, lebar = gambar.shape[:2]

# Menghitung ukuran data gambar (dalam byte)
ukuran_data = gambar.size

# Mendapatkan tipe data gambar
tipe_data = gambar.dtype

# Menampilkan informasi gambar
print(f"Resolusi gambar: {tinggi}x{lebar}")
print(f"Ukuran data: {ukuran_data} bytes")
print(f"Tipe data: {tipe_data}")
