"""
Data types
"""

myString = " This is a string. "
print(myString)
print(type(myString))
print(myString + " is the data type of " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("what is your name?: ")
print(name)
print("hello " + name)
color = input("what is your favorite color: " )
animal = input("what is your favorite animal?: ")
print("{}, you like {} {}!".format(name,color,animal))