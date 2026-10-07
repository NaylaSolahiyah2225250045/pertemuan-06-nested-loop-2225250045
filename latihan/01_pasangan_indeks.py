# Loop luar: mengatur nilai i dari 1 sampai 3.
# Loop dalam: mengatur nilai j dari 1 sampai 4.
# Counter: menghitung banyak pasangan yang ditampilkan.

count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

# Kondisi: loop berhenti setelah semua nilai i dan j selesai.
# Output: menampilkan semua pasangan dan jumlah pasangan.
print(f"Banyak pasangan yang ditampilkan: {count}")