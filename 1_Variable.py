# gabungan diantara 4 jenis nilai variable tersebut 

name = "zikri"
number = 6212345678
price = 1490.90
want_to_buy = True

# the code will check this first function
# the event if the price is too expensive or not

if price < 150:
    want_to_buy = True
else:
    want_to_buy = False

    print("because the price is too expensive")

# the event if the custumer want to buy the product or not

if want_to_buy:
    print(F"Hello my name is {name}, from number {number}, im interasted to buy this product with price $ {price}")
else:
    print("no one buy the product")

