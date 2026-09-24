while True:
    try:
        N = int(input("Masukkan jumlah kursi bus: "))

        sisa_kursi = N
        total_pendapatan = 0

        while sisa_kursi > 0:

            try:
                umur = int(input("Masukkan umur penumpang: "))

                if umur < 0:
                    print("Umur tidak valid!")
                    continue

                if umur <= 5:
                    harga = 0
                    print("Tiket Gratis")

                elif umur <= 12:
                    harga = 50000
                    print("Tiket Anak: Rp 50000")

                else:
                    harga = 100000
                    print("Tiket Dewasa: Rp 100000")

                total_pendapatan += harga
                sisa_kursi -= 1

                print("Tiket berhasil diproses!")
                print("Sisa kursi:", sisa_kursi)

            except ValueError:
                print("Umur harus berupa angka!")

        print("Total pendapatan bus: Rp", total_pendapatan)

    except ValueError:
        print("Jumlah kursi harus berupa angka!")