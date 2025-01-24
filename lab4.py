myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

anotherTuple = ("1", 2, "Monday", 123, 1.4 , "Tuesday")
print("this is another tuple" + str(anotherTuple))

myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Tatiana": "pineapple",
    "Paulo": "mango"
}
print(myFavoriteFruitDictionary)
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Tatiana"][4:]) # slice starts at index 4
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary["Paulo"][::-1]). # slice starts from the back