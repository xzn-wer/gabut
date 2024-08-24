print("="*30)
print("      KALKULATOR ALAKADAR")
print("="*30)

angka_1 = float(input("masukan angka pertama\t : "))
operator = input("operator (+,-,*,/)\t : ")
angka_2 = float(input("masukan angka ke dua :"))

if operator=="+":
    hasil = angka_1 + angka_2
    print(f"hasil = {hasil:.2f}")
elif operator=="-":
    hasil = angka_1 - angka_2
    print(f"hasil = {hasil:.2f}")
elif operator=="*":
    hasil = angka_1 * angka_2
    print(f"hasil = {hasil:.2f}")
elif operator=="/":
    hasil = angka_1 / angka_2
    print(f"hasil = {hasil:.2f}")
else:
    print("operator yg anda masukan failed")