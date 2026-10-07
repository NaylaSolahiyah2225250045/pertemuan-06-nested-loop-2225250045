n = int(input("n: "))

# Counter: menghitung banyak pasangan yang memenuhi kondisi.
count = 0

# Loop luar: menentukan nilai i dari 1 sampai n.
for i in range(1, n + 1):

    # Loop dalam: menentukan nilai j dari 1 sampai n.
    for j in range(1, n + 1):

        # Kondisi: pasangan dihitung jika i + j <= n.
        if i + j <= n:
            count += 1

# Output: menampilkan banyak pasangan yang memenuhi kondisi.
print(f"Banyak pasangan = {count}")