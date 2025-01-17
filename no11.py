import cv2
import matplotlib.pyplot as plt

# Membaca gambar
gambar = cv2.imread('muhfi.jpeg')

# Konversi gambar ke ruang warna HSV
hsv = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV)

# Memisahkan channel hue, saturation, dan value
h, s, v = cv2.split(hsv)

# Menghitung histogram untuk setiap channel
hist_hue = cv2.calcHist([h], [0], None, [256], [0, 256])
hist_saturation = cv2.calcHist([s], [0], None, [256], [0, 256])
hist_value = cv2.calcHist([v], [0], None, [256], [0, 256])

# Menampilkan histogram
plt.figure(figsize=(10, 6))
plt.plot(hist_hue, color='r', label='H')
plt.plot(hist_saturation, color='g', label='S')
plt.plot(hist_value, color='b', label='V')
plt.title('HSV histogram')
plt.xlabel('intensitas')
plt.ylabel('frequensi')
plt.legend()
plt.grid()
plt.show()