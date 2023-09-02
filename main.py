# Write a Python program that asks the user to enter an integer and then determines whether that integer is even or odd. After the user inputs the integer, the program should print "Even" if it's even and "Odd" if it's odd.


# my most pythonic implementation

integer = int(input("Enter your number: "))
def odd_even(integer):
  if integer % 2 == 0:
    return "Even"
  elif integer % 2 == 1:
    return "Odd"

result = odd_even(integer)
print(result)