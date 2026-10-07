n = int(input("n: "))

# Loop luar: menentukan baris dari 1 sampai n.
# Loop dalam: mencetak bintang sebanyak nomor baris.
# Counter/akumulator: tidak digunakan.

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Kondisi: loop berhenti setelah n baris selesai.
# Output: menampilkan pola bintang berbentuk segitiga.