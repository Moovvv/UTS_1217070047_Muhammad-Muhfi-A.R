import cv2

# Membaca gambar
image = cv2.imread('muhfi.jpeg')

# Konversi gambar ke ruang warna HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Memisahkan hue, saturation, dan value
hue = hsv[:,:,0]
saturation = hsv[:,:,1]
value = hsv[:,:,2]

# Menampilkan gambar hue, saturation, dan value
cv2.imshow('Hue', hue)

# Menunggu penekanan tombol untuk keluar
cv2.waitKey(0)

# Menutup jendela
cv2.destroyAllWindows()
