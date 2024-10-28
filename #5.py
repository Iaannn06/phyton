#5 

def cetak_angka(n):
    for i in range(1, n+1):
        print(str(i) *i)

n = int(input("Masukkan nilai yang diinginkan = "))
print("Angka yang dihasilkan adalah= ")
cetak_angka(n)

for i in range(3): 
    if i == 1: 
        break 
    print(i)

x = 5 
while x > 0: 
    x -= 1
    