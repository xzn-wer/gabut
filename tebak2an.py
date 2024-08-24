import random

welcome_massage = "selamat datang"
tikus_position = random.randint(1,4)

print("="*30)
print(f'========{welcome_massage}========')
print("="*30)

nama_user = input("masukan nama kamu : ")
while nama_user == "":
    nama_user = input("masukin namamu : ")


bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4
goa = goa_kosong.copy()
goa[tikus_position -1] = "|0-0|"
goa_kosong = " ".join(goa_kosong)


print(f'''halo {nama_user}! liat goa dibawah
{goa_kosong}''')

pilihan_user = int(input("menurut lu di angka berapa tikus berada 1/2/3/4 :"))
if pilihan_user < 5 and pilihan_user > 0:
    print('')
else:
    print('pilihan tak valid')
    exit()

konfirmasi = input(f'lu yakin milih {pilihan_user} ? [y/n] ')
if konfirmasi == "n":
    print('program dihentikan')
    exit()
elif konfirmasi == "y":
    if pilihan_user == tikus_position:
        print(f'{" ".join(goa)} \n lu bener karena lu hoki milih {tikus_position}')
    else:
        print(f'{" ".join(goa)} \n lu salah,karena tikus ada di nomer {tikus_position}')
        exit()
else:
    print('pilihan tidak valid')
    exit()







