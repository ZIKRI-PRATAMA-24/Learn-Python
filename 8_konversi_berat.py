berat = float(input("masukkan berapa berat bendanya: "))
benda = input("Kilograms atau pounds? (K/L):")

if benda == "K":
    beratnya = berat * 2.205
    unit = "Lbs."
    print(f"benda anda telah dikonversikan beratnya menjadi {round(beratnya, 2)} {unit}")
elif benda == "L":
    beratnya = berat / 2.205
    unit = "Kg."
    print(f"benda anda telah dikonversikan beratnya menjadi {round(beratnya, 2)} {unit}")
else:
    print("invalid, tolong pilih K/L")
    

