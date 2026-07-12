barang = input("masukan nama barang: ")
harga = float(input("masukan harga barang: "))
jumlah = int(input("masukan jumlah barang: "))

total = harga * jumlah

print(f"kamu telah membeli {barang} sebanyak {jumlah}")
print(f"dengan total harga: $ {total}")