#4
def angka_ganjil(n):
    ganjil = [i for i in range(1, n + 1) if i % 2 != 0]
    print("Angka ganjil hingga n adalah:", ganjil)

n = int(input("Masukkan nilai n yamg diinginkan: "))
angka_ganjil(n)
