

print("|================================|")
print("|      PROGRAM KASIR RAMAH       |")
print("|================================|")
print("|       PILIH MENU MAKANAN       |")
print("|================================|")
print("|ayam bakar              Rp.15000|")
print("|ayam geprek             Rp.15000|")
print("|nasgor                  Rp.20000|")
print("|nasi pecel              Rp.10000|")
print("|soto ayam               Rp.12000|")
print("|================================|")

nomer_makanan = int(input("pilih menu yg ada aja y njing (1/2/3/4/5) : "))
jml_porsi = int(input("mau pesen brp bitch? : "))

if nomer_makanan == 1:
    total_makanan = jml_porsi * 15000
    print(f'ayam bakar {jml_porsi} porsi Rp.{total_makanan}')
    makanan = 'ayam bakar'
    
elif nomer_makanan == 2:
    total_makanan = jml_porsi * 15000
    print(f'ayam geprek {jml_porsi} porsi Rp.{total_makanan}')
    makanan = 'ayam geprek'
    
elif nomer_makanan == 3:
    total_makanan = jml_porsi * 20000
    print(f'nasgor {jml_porsi} porsi Rp.{total_makanan}')
    makanan = 'nasgor'

elif nomer_makanan == 4:
    total_makanan = jml_porsi * 10000
    print(f'nasi pecel {jml_porsi} porsi Rp.{total_makanan}')
    makanan = 'nasi pecel'
    
elif nomer_makanan == 5:
    total_makanan = jml_porsi * 12000
    print(f'soto ayam {jml_porsi} porsi Rp.{total_makanan}')
    makanan = 'soto ayam'

else:
    print('kata gua juga yg ada aja ajg :v')
    exit()





print("|================================|")
print("|================================|")
print("|           PILIH MINUMAN        |")
print("|================================|")
print("|teh tawar                   3000|")
print("|kopi susu                   8000|")
print("|es milo                    13000|")
print("|lemon tea                   8000|")
print("|es jeruk                    5000|")
print("|================================|")

nomer_minuman = int(input("pilih minuman biar ga ceket (1/2/3/4/5) : "))
jml_gelas = int(input('mau berapa gelas hoee? : '))


if nomer_minuman == 1:
    total_minuman = jml_gelas * 3000
    print(f"teh tawar {jml_gelas} gelas Rp.{total_minuman}")
    minuman = "teh tawar"

elif nomer_minuman == 2:
    total_minuman = jml_gelas * 8000
    print(f"kopi susu {jml_gelas} gelas Rp.{total_minuman}")
    minuman = "kopi susu"

elif nomer_minuman == 3:
    total_minuman = jml_gelas * 13000
    print(f"es milo {jml_gelas} gelas Rp.{total_minuman}")
    minuman = "es milo"

elif nomer_minuman == 4:
    total_minuman = jml_gelas * 8000
    print(f"lemon tea {jml_gelas} gelas Rp.{total_minuman}")
    minuman = "lemon tea"
    
elif nomer_minuman == 5:
    total_minuman = jml_gelas * 5000
    print(f"es jeruk {jml_gelas} gelas Rp.{total_minuman}")
    minuman = "es jeruk"

else :
    print('minuman gada kontol')
    exit()



total_semua = total_makanan + total_minuman
print(f"lu harus bayar segini Rp.{total_semua}")

bayar = int(input('bayar yg pas y jing : '))

if bayar >= total_semua:
    kembalian = bayar - total_semua
else:
    duit_kurang  = total_semua - bayar
    print("duit lu kurang goblok")
    exit()



print("|================================|")
print("|================================|")
print("|        STRUK PEMBELIAN         |")
print("|================================|")
print("|makanan            :",makanan,"\t")
print("|jumlah porsi       :",jml_porsi,"\t\t\t")
print("|minuman            :",minuman,"\t\t")
print("|jumlah gelas       :",jml_gelas,"\t\t\t")
print("|total pembayaran   :",total_semua,"\t\t")
print("|bayar              :",bayar,"\t\t")
print("|kembalian          :",kembalian,"\t\t")
print("|================================|")





