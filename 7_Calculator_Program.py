# calculator program

operator = input("Pilihlah salah satu operator (+ - * / ^): ")
num1 = float(input("Masukin angka pertama: "))
num2 = float(input("Masukin angka kedua: "))

if operator == "+":
    jumlah = num1 + num2
    print(jumlah)
elif operator == "-":
    jumlah = num1 - num2
    print(jumlah)
elif operator == "*":
    jumlah = num1 * num2
    print(jumlah)
elif operator == "/":
    jumlah = num1 / num2
    print(jumlah)
elif operator == "^":
    jumlah = pow(num1, num2)
    print(jumlah)
else:
    print("ERROR!, Tolong pilih operator yg tersedia") 
    