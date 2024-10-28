#3
def fibonacci(n):
    a, b = 0, 1
    deret = []
    while a < n:
        deret.append(a)
        a, b = b, a + b
    print("Angka-Angka fibonacci hingga n:", deret)

n = int(input("masukkkan angka anda:"))
fibonacci(n)