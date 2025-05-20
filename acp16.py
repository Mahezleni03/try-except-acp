try:
   age = int(input("Enter your age :"))

except ValueError:
   print("Please enter a number")

if age == 0:
   print("Your age is an even number")
else:
   print("Your age is a odd number")