print("="*15)
print("MENGHITUNG BMI")
print("="*15)


berat_badan = float(input("masukan berat badan (kg) : "))
tinggi_badan = float(input("masukan tinggi badan (cm) : "))

tinggi_badan = tinggi_badan/100
bmi = berat_badan/(tinggi_badan**2)

if bmi < 18.5:
    status = "anda kurang berat badan"
elif bmi >= 18.5 and bmi <= 22.9:
    status = "normal"
elif bmi >= 23 and bmi <= 24.9:
    status = "kelebihan berat badan"
elif bmi >= 25 and bmi <= 29.9:
    status = "obesitas level 1"
elif bmi > 30:
    status = "obesitas level 2"


print(f'BMI = {bmi:.2f}')
print('status = ', status)