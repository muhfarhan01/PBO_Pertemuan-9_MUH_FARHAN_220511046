class KonversiSuhu:
    def __init__(self, suhu):
        self.suhu = suhu

    def to_fahrenheit(self):
        return (9/5 * float(self.suhu)) + 32

    def to_reamur(self):
        return (4/5 * float(self.suhu))

    def to_kelvin(self):
        return float(self.suhu) + 273

print("Konversi Suhu Celcius")

# Input
suhu_celcius = input("Masukkan suhu dalam Celcius: ")

# Membuat objek KonversiSuhu
konversi = KonversiSuhu(suhu_celcius)

# Melakukan konversi
F = konversi.to_fahrenheit()
R = konversi.to_reamur()
K = konversi.to_kelvin()

# Output
print(suhu_celcius + " Celcius sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")

