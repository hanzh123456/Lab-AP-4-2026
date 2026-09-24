while True:
    try:
        N = int(input("Masukkan jumlah baris: "))
        M = int(input("Masukkan jumlah kursi: "))

        for baris in range(1, N + 1):
            for kursi in range(1, M + 1):

                if kursi == 13:
                    continue

                if baris == 1 and kursi % 2 == 0:
                    continue

                print(f"Baris {baris}, Kursi {kursi}")

    except ValueError:
        print("Input harus berupa angka!")


