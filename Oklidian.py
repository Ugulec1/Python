# 1. Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# 2. 2D uzaydaki noktaları temsil eden 'points' listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# 3. Mesafelerin saklanacağı 'distances' listesi
distances = []

# 4. Döngü kullanarak her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çiftleri tekrar hesaplamamak için j, i + 1'den başlar
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)  # Sadece mesafeleri ekle

# 5. Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
