cabai = int(input("Masukkan persentase cabai: "))

if cabai < 0:
    print("Input tidak valid")
elif cabai <= 10:
    print("Level Aman")
elif cabai <= 40:
    print("Level Sedang")
elif cabai <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")