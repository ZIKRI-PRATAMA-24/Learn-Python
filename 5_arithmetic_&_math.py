# A = 10

# A += 2
# A -= 2
# A *= 2
# A /= 2
# A **= 2

# print(A)

# X = 3.14
# Y = -3
# Z = 4

# hasil = round(X) # pembulatan angka
# hasil = abs(Y) # nilai absolut
# hasil = pow(Z, 2) # pangkat
# hasil = max(X, Y, Z) # nilai terbesar
# hasil = min(X, Y, Z) # nilai terkecil

# print(hasil) 

import math

# X = 16
# Y = 9.1


# nilai = math.pi  # menampilkan nilai pi
# nilai = math.e # menampilkan nilai euler/konstanta
# nilai = math.sqrt(X) # menampilkan nilai akr kuadrat dari X
# nilai = math.ceil(Y) # menampilkan nilai pembulatan ke atas
# nilai = math.floor(Y) # menampilkan nilai pembulatan ke bawah

# print(nilai)



# rumus lingkaran

# R = float(input("masukin nilai jari-jari lingkaran: "))

# kelilingLingkaran = 2 * math.pi * R

# print(F"keliling lingkarannya adalah {round(kelilingLingkaran, 2)} cm ")


# rumus luas lingkaran

# R = float(input("masukan nilai jari-jari lingkaran: "))

# luasLingkaran = math.pi * pow(R, 2)

# print(f"luas lingkarannya adalah {round(luasLingkaran, 2)} cm²")


# rumus pyhtagoras

A = float(input("masukin nilai sisi A: "))
B = float(input("masukin nilai sisi B: "))

C = math.sqrt(pow(A, 2) + pow(B, 2))

print(f"nilai sisi C adalah {round(C, 2)} cm")