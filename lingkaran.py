print("=======MENGHITUNG KELILING=======")

r = float(input("masukan nilai jari-jari : "))
phi = 3.14
diameter = 2*r

# MENGHITUNG LUAS
luas = phi*r*r
# MENGHITUNG KELILING
keliling = 2*phi*r

print("\nluas lingkaran         = ", str("%.2f" % luas))
print("keliling lingkaran       = ", str("%.2f" % keliling))
