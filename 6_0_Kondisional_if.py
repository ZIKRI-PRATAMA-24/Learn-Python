# contoh sederharna penggunaan kondisional if

umur = int(input("masukin umur anda: "))

if umur >= 100:
    print("kamu terlalu tua untuk diterima bekerja disini")
elif umur >= 18:
    print("kamu diterima bekerja disini")
elif umur <= 0:
    print("kamu bahkan belum lahir")
else:
    print("kamu terlalu muda untuk diterima bekerja disini")