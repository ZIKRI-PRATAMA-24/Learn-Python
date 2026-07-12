# contoh input

nama = input( "what is your name?: ")
# age = int(input("how old are you?: ")) bisa ubah langsung ke int tanpa harus di casting
age = input("how old are you?: ")

age = int(age) # casting ke int
age = age + 1

print(f"Hello {nama}!")
print("Happy Birtday!")
print(f"You are {age} years old now!")
