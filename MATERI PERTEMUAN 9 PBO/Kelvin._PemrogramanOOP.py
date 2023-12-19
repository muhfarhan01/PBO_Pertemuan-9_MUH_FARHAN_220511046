class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def to_kelvin(self):
        return float(self.suhu)

    def to_fahrenheit(self):
        return (9/5 * float(self.suhu)) + 32

    def to_reamur(self):
        return (4/5 * float(self.suhu))

    @staticmethod
    def reamur_to_kelvin(reamur):
        return (5/4 * reamur) + 273.15

print("Konversi Suhu kelvin")

# Input
suhu_kelvin = input("Masukkan suhu dalam kelvin: ")

# Membuat objek KonversiSuhu
konversi = Kelvin(suhu_kelvin)

# Melakukan konversi
F = konversi.to_fahrenheit()
R = konversi.to_reamur()
K = konversi.to_kelvin()
C_from_R = Kelvin.reamur_to_kelvin(R)

# Output
print(suhu_kelvin + " Kelvin sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
print(str(C_from_R) + " Kelvin (dari Reamur)")
        
    