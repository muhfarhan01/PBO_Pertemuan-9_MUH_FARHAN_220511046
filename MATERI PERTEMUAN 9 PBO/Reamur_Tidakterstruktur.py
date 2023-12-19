print("Konversi Suhu Reamur")

# Input
suhu = input("Masukkan suhu dalam Reamur: ")

# Konversi ke Fahrenheit
F = (9/4 * float(suhu)) + 32

# Konversi ke Reamur
R =  float(suhu)

# Konversi ke Kelvin
K = 5/4 * float(suhu) + 273

# Konversi dari Reamur ke Celcius
C = (5/4) * R

# Output
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
print(str(C) + " Celcius (dari Reamur)")
