# Document String (DOC STRING)
# def -> Reserved keyword (Built-in keywords in python and should not be used as a variable name!)
def loopFunction(turSayisi) -> list:
    '''
    Single quotes
    This code generates the numbers starting from 0 to turSayisi variable
    The function takes the parameter named 'turSayisi'
    And returns each number within a list
    return type : list
    '''

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
