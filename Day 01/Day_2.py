#exercise 2 shpping cart programe

item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like?: "))
total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")