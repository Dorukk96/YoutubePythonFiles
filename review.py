# OVERVIEW

# Liste methodları (3 questions)
# fonksiyonlar (2 questions) 1 fonk. - 1 lambda fonk.
# algoritma (asal sayıları veren / fibonacci sayiları)
# Dictionaries -> Map (from other programming languages)

# sorting
# 3, 5, 6, 1, 9
# 3, 5, 1, 6, 9
# 3, 1, 5, 6, 9
# 1, 3, 5, 6, 9
myList: list = [2, 5, 7, 3, 1, -5, -100, 14, 45, 67, 33]
print(f"My current list : {myList}")
myList.sort()
print(f"My updated list : {myList}")

favoriteFruits: list = ["Apple", "Grapes", "Banana", "Watermelon", "Fig"]
print(f"My current fruit list : {favoriteFruits}")
favoriteFruits.sort() # Alphabetical order
print(f"My updated fruit list : {favoriteFruits}")
favoriteFruits.reverse()
print(f"My reversed fruit list : {favoriteFruits}")
# favoriteFruits.append("Strawberry")
# print(f"My list : {favoriteFruits}")
favoriteFruits.pop()
print(f"my list : {favoriteFruits}")
favoriteFruits.remove("Grapes")
print(f"my list : {favoriteFruits}")


# Functions Overview
mixedDataTypedList = [1, 3, 'a', True, [2, 5, 'f'], (45, 45), 3.14, 2.7172, False] # 9

def listLineByLine1(listParam):
    for listIndex in range(len(listParam)):
        print(listParam[listIndex])

def listLineByLine2(lstPrm):
    for eachItem in lstPrm:
        print(eachItem)


listLineByLine1(mixedDataTypedList)
print("===========================")
listLineByLine2(mixedDataTypedList)


# Lambda function
# ax2 + bx + c
def parabolFunc(a: float, b: float, c: float):
    return lambda x : (a*x**2 + b*x + c)

f = parabolFunc(2, 3, 4)
print(f(10))
# 2*10**2 + 3*10 + 4 = 234 """


# algoritma (asal sayıları veren / fibonacci sayiları)
# FIBONACCI SAYILARINI VEREN ALGORITMA

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ....
def createFiboList(numberOfItem):
    fiboList = []
    fiboItem1, fiboItem2 = 0 , 1
    for i in range(numberOfItem):
        fiboList.append(fiboItem1)
        fiboItem1, fiboItem2 = fiboItem2, fiboItem1 + fiboItem2
    
    # Phi (altın oran / golden ratio)
    print(fiboItem1 / fiboItem2) # 0.618...... / 0.6180339887498949
    return fiboList

print(createFiboList(80))

# Dictionaries -> Map (from other programming languages)
# Dictionary is a datatype 
engTur: dict = {
    'book' : 'kitap', # key-value pair
    'pencil' : 'kalem',
    'eraser' : 'silgi',
    'ruler' : 'cetvel'
}

# for kw in engTur:
#     print(f"{kw} is {engTur[kw]}")

brandSalesSummaryDict: dict = {
    'Apple' : 500,
    'Samsung': 350,
    'Huawei' : 300,
    'Xiaomi': 400,
    'Nokia': 100
}

# sum all the stock values up in this dict.
total: int = 0
for eachBrand in brandSalesSummaryDict:
    print(f"{eachBrand} has only {brandSalesSummaryDict[eachBrand]} in stock.")
    total += brandSalesSummaryDict[eachBrand]

print(f"We have {total} products in total.")

userInfoDict = {
    # key : value
    # name : [lastname, age, height, weight, education]
    'John' : ['Smith', 24, 1.87, 78.8, 'University'],
    'Wilma': ['Sonn', 45, 1.65, 57.7, 'Master'],
    'Jonathan': ['Semy', 17, 1.77, 68, 'High school'],
    'Mark' : ['William', 34, 1.80, 75.3, 'University'],
    'Jeff': ['Helly', 50, 1.90, 84, 'Master']
}

# Take all the ages, heights, weights. And then sum them up.
# Then print all the results

totalAge: int = 0
totalHeight: float = 0
totalWeight: float = 0
for eachUser in userInfoDict:
    totalAge += userInfoDict[eachUser][1]
    totalHeight += userInfoDict[eachUser][2]
    totalWeight += userInfoDict[eachUser][3]
print(f"Total age of all the users is {totalAge},\nTotal height of all the users is {totalHeight},\nAnd total weight of all the users is {totalWeight}")


ageSumUni: int = 0
ageSumMs: float = 0
ageSumHs: float = 0
# Only sum all the ages up if the education level is University
# Do the same calculation for Master and High school
for eachUser in userInfoDict:
    # if userInfoDict[eachUser][-1] == 'University':
    #     ageSumUni += userInfoDict[eachUser][1]
    # elif userInfoDict[eachUser][-1] == 'Master':
    #     ageSumMs += userInfoDict[eachUser][1]
    # elif userInfoDict[eachUser][-1] == 'High school':
    #     ageSumHs += userInfoDict[eachUser][1]
    # else:
    #     print("No such education level")

    match userInfoDict[eachUser][-1]:
        case 'University':
            ageSumUni += userInfoDict[eachUser][1]
        case 'Master':
            ageSumMs += userInfoDict[eachUser][1]
        case 'High school':
            ageSumHs += userInfoDict[eachUser][1]
        case _:
            print("No such education level")


print(f"total ages for university : {ageSumUni}")
print(f"total ages for master : {ageSumMs}")
print(f"total ages for high school : {ageSumHs}")