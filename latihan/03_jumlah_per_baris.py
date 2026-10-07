# Loop luar: menentukan nilai i dari 1 sampai 4.
for i in range(1, 5):
    total_baris = 0

    # Loop dalam: menentukan nilai j dari 1 sampai 3.
    for j in range(1, 4):
        total_baris += i * j

    # Akumulator: total_baris menjumlahkan nilai i * j pada setiap baris.
    # Kondisi: loop berhenti setelah j mencapai 3 dan i mencapai 4.
    # Output: menampilkan jumlah setiap baris.
    print(f"Jumlah baris {i} = {total_baris}")