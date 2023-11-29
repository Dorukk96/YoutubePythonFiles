# Match Statement
def http_error(status) -> str:
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# if - else usage
def http_error_if_else(status) -> str:
    if(status == 400):
        return "Bad request"
    elif (status == 404):
        return "Not found"
    elif(status == 418):
        return "I'm a teapot"
    else:
        return "Something's wrong with the internet"

print(f"if error code is 400 : {http_error_if_else(400)}")
print(f"if error code is 404 : {http_error_if_else(404)}")
print(f"if error code is 418 : {http_error_if_else(418)}")
print(f"if error code is 419 : {http_error_if_else(419)}")

def http_error2(status) -> str:
    match status:
        case 401 | 403 | 404 | 405:
            return "Not allowed"

# print(http_error(405))
# print(http_error(400))
# print(http_error(404))
# print(http_error(418))
# print(http_error(419))

# point is an (x, y) tuple
# python -> match Statement
# java, js, c c++ -> switch statements

def cartesianSystem(point: tuple):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
def cartesianSystem_ifElse(x: float, y: float):
    point: tuple = (x, y)
    if point == (0, 0):
        print("Origin")
    elif point == (0, y):
        print(f"Y={y}")
    elif point == (x, 0):
       print(f"X={y}")
    elif point == (x, y):
        print(f"X={x}, Y={y}")
    else:
        raise ValueError("Not a point")

cartesianSystem_ifElse(0, 0)
cartesianSystem_ifElse(0, 5)
cartesianSystem_ifElse(-9, -5)

# ikiliNokta1 = (4, 6)
# ikiliNokta2 = (6, 9)        

# cartesianSystem(ikiliNokta1)
# cartesianSystem(ikiliNokta2)
# cartesianSystem((2, 3, 4))

# HARF NOTU HESAPLAMA
# 100 - 85 -> A
# 85 - 70 -> B
# 70 - 55 -> C
# 55 - 40 -> D
# 40 - 25 -> E
# 25 - 0 -> F

def harfNotuHesaplama(harfNotu: float) -> str:
    match harfNotu:
        case harfNotu if 85 <= harfNotu <= 100:
            return "A"
        case harfNotu if 70 <= harfNotu < 85:
            return "B"
        case harfNotu if 55 <= harfNotu < 70:
            return "C"
        case harfNotu if 40 <= harfNotu < 55:
            return "D"
        case harfNotu if 25 <= harfNotu < 40:
            return "E"
        case harfNotu if 0 <= harfNotu < 25:
            return "F"
        case _:
            raise ValueError("You CANNOT enter a point less than 0 and more than 100")

print('Harf Notunuz : ' + harfNotuHesaplama(90))
print('Harf Notunuz : ' + harfNotuHesaplama(74))
print('Harf Notunuz : ' + harfNotuHesaplama(56))
print('Harf Notunuz : ' + harfNotuHesaplama(30))
print('Harf Notunuz : ' + harfNotuHesaplama(15))
print('Harf Notunuz : ' + harfNotuHesaplama(45.9))
# print('Harf Notunuz : ' + harfNotuHesaplama(-1))
