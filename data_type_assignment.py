#  Integer
# data type having whole numbers
age=16
print("In 5 years, your age will be", age+5)

# String
# A String is a collection of characters, words, or sentences enclosed in quotes.
name="Sajjad"
greeting="Hello,"" "+ name
print(greeting)

# Float
# whole numbers having decimal are called float.
height=1.65 # in meters
print("Your height is",height, "meters.")

#  Combined Use
item="Football" # string
quantity=4 # integer
price_per_item=19.9 # float
total_cost=quantity*price_per_item
print("You bought 4 Footballs for a total of",total_cost,"dollars")


# Challenge Yourself!

name=input("Please Enter Your Name:   ")
item=input("An item want to by:   ")
price=float(input("Price of the item:   "))
quantity=int(input("Quantity:   "))
total_price=price*quantity
print(f"\nHello, {name} \nYou bought {quantity} {item}s.\nTotal: {total_price:.2f} dollars.\nThank You for Shopping")
