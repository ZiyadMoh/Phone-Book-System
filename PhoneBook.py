#Phone Book Dictionary
Book = {'Amal':'1111111111', 'Mohammed':'2222222222', 'Khadijah':'3333333333', 'Abullah':'4444444444', 'Rawan':'5555555555', 'Faisal':'6666666666', 'Layla':'7777777777'}

#number length validation

def checkNum(num):
    if(len(number) < 10 or len(number) > 10):
        while len(number) < 10 or len(number) > 10:
            print('This is invalid number')
            CorrNumber = input('Please Enter a valid number: ')
        return number    
#search Number
def searchNum(num):
    for name, Snumber in Book.items():
        if number == Snumber:
            return name    
    print('Sorry, the number is not found ')
            
            
#Test
number = input("Enter Phone Number: ")
CorrNum = checkNum(number)
searchNum(CorrNum)
