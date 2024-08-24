awal = int(input("masukan angka awal : "))
akhir = int(input("masukan angka akhir : ")) 

x = []
y = []

for i in range(awal,akhir+1):
    if i%2 == 0:
        x.append(i)
    if i%2 == 1:
        y.append(i)
print('angka genap : ', x)
print("angka ganjil : ", y)
