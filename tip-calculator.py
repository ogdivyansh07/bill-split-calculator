print("Welcome To Tip Calculator")
a = int(input("What was the total bill = ₹"))
b = int(input("How much tip would you like to give like 5% , 10% or 15% = "))
c= int(input("How many person to split the bill = "))
d=(((b/100)*a)+a)/c
print(f"each person should pay ={round(d,2)}")