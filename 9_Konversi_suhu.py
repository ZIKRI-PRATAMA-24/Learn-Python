Suhu = input("apakah ini suhu Celsius atau Fahrenheit (C/F): ")
Temperatur = float(input("masukkan nilai temperatur nya: "))

if Suhu == "C":
    Konversi = (Temperatur * 9/5) + 32
    unit = "F"
    print(f"hasilnya, {Temperatur}°{Suhu} = {round(Konversi)}°{unit}")
elif Suhu == "F":
    Konversi = (Temperatur - 32) * 9/5
    unit = "C"
    print(f"hasilnya, {Temperatur}°{Suhu} = {round(Konversi)}°{unit}")
else:
    print("ERROR!, Tolong pilih C/F")
