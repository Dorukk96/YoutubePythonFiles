# Document String (DOC STRING)
# def -> Reserved keyword
def loopFunction(turSayisi) -> list:
    """
    Single quotes
    This code generates the numbers starting from 0 to turSayisi variable
    The function takes the parameter named 'turSayisi'
    And returns each number within a list
    return type : list
    """

    """
        This code generates the numbers starting from 0 to turSayisi variable
        The function takes the parameter named 'turSayisi'
        And returns each number within a list
        return type : list
    """

    numberList = []
    for i in range(0, turSayisi):
        numberList.append(i)

    return numberList


print(loopFunction.__doc__)
print(loopFunction(40))




def sayHiToUser(userName: str, userAge: int) -> str:
    greeting = 'Hello, ' + userName.capitalize() + '. You are ' + str(userAge) + ' years old.'
    return greeting

print(sayHiToUser('doruk', 27))

def summation(num1: int, num2: int, isEven: bool) -> float:
    total = 0
    for i in range(num1, num2): # 0, 1, 2, ... 9
        if isEven and i % 2 == 0:
            total += i # 45
        if not isEven and i % 2 == 1:
            total += i # 45
    return total

print(summation(0, 10, False)) # 1, 3, 5, 7, 9 -> 25
print(summation(0, 10, True)) # 0, 2, 4, 6, 8 -> 20

# .....x.....
# ....xxx....
# ...xxxxx...
# ..xxxxxxx..
# .xxxxxxxxx.
# xxxxxxxxxxx
# .xxxxxxxxx.
# ..xxxxxxx..
# ...xxxxx...
# ....xxx....
# .....x.....

def dimondShape(char1: str , char2: str, turSayisi: int):

    if turSayisi % 2 == 1:
        firstLoop: int = int(((turSayisi - 1) / 2) + 1)
        secondLoop: int = int((turSayisi - 1) / 2)
        numberOfChar: int = 1
        numberOfDots: int = firstLoop - 1
        for i in range(firstLoop):
            print(char1 * numberOfDots + char2 * numberOfChar + char1 * numberOfDots)
            numberOfDots -= 1
            numberOfChar += 2
            if numberOfDots < 0:
                break
        numberOfDots = 1
        numberOfChar = turSayisi - 2
        for j in range(secondLoop):
            print(char1 * numberOfDots + char2 * numberOfChar + char1 * numberOfDots)
            numberOfDots += 1
            numberOfChar -= 2
    else:
        print('Please, enter an odd number!!!')
# dimondShape('..','A', 11)

fruitList = ['apple', 'banana', 'orange', 'grape', 'melon']
randomList = [1, 3.4, True, [1,2,3], (4, 7, 12), 'Hello']

def elementsOfFruitList():
    for eachFruit in fruitList:
        print(eachFruit)

elementsOfFruitList()


class Fruit:
    fruitName = ''
    fruitColor = 'Yeşil'


    def sayHi(self, userName: str) -> str:
        greeting = 'Hello, ' + userName.capitalize()
        return greeting
    
    def calculateAge(self, dateOfBirth: int):
        currentYear = 2023
        yourAge = currentYear - dateOfBirth
        print('Your age is ' + str(yourAge))

    def changeFruitColor(self, newColor: str) -> str:
        self.fruitColor = newColor
        return self.fruitColor
    
    def turnNumbersIntoTuple(self, pos1: float, pos2: float) -> tuple:
        myTuple = (pos1, pos2)
        return myTuple
fruit1 = Fruit()
print(fruit1.sayHi('michael'))
fruit1.calculateAge(1996)
print('New fruit color is ' + fruit1.changeFruitColor('Red'))
print('My Tuple : ' + str(fruit1.turnNumbersIntoTuple(1.46, 3.14)))

# create class named Circle
class Circle:
    diameter = 0
    PI = math.pi

    # Cevre : 2 * pi * yaricap
    def cevreHesaple(self, yaricap: float) -> str:
        result = 2 * self.PI * yaricap
        return 'Girilen yarıçapa göre cevre uzunluğu : ' + str(result)
    
    # Alan : PI * yaricap^2
    def alanHesapla(self, yaricap: float) -> str:
        result = self.PI * yaricap * yaricap
        return 'Girilen yarıçapa göre alan değeri : ' + str(result)
circle1: Circle = Circle()
print('Pi sayisinin degeri : ' + str(circle1.PI))
print(circle1.cevreHesaple(10))
print(circle1.alanHesapla(10))
print('Cos(0) = ' + str(math.cos(0)) + ', type : ' + str(type(math.cos(0))))
print('sin(0) = ' + str(math.sin(0)) + ', type : ' + str(type(math.sin(0))))
print('tan(0) = ' + str(math.tan(90)) + ', type : ' + str(type(math.tan(90))))
print('tan(90) = ' + str(1/(math.tan(90))) + ', type : ' + str(type(1/(math.tan(90)))))

