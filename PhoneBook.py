#Phone Book Dictionary
Book = {'Amal':'1111111111', 'Mohammed':'2222222222', 'Khadijah':'3333333333', 'Abullah':'4444444444', 'Rawan':'5555555555', 'Faisal':'6666666666', 'Layla':'7777777777'}

#number length validation

def checkNum(num):
        while len(num) < 10 or len(num) > 10:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('\nThis is invalid number \n')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            num = input('Please Enter a valid number: ')
        return num    
#search by Number
def searchNum(num):
    for name, Snumber in Book.items():
        if num == Snumber:
            print('------------------------------')
            print('\n'+name+'\n')
            print('------------------------------')
            return     
    print('Sorry, the number is not found ')
    
    
#search by Name            
def searchName(name):
    for Sname, number in Book.items():
        if Sname == name:
            print('------------------------------')
            print('\n'+number+'\n')
            print('------------------------------')
            return 
    print('The Entered name does not exist')

#add Conatact    
def addCont(name,phone):
    Book[name] = phone
    print('\nContact Was Added Successfully...')

''' Test
number = input("Enter Phone Number: ")
CorrNum = checkNum(number)
searchNum(CorrNum)
'''


#system simulation
print('##############################################################')
print('\nWelcom to your Phone Book..\n')
while True:
    print('\nPleasea select one of the options below.. ')
    print('1.Search Name By Number \n2.Search Number By Name \n3.Add A New Contacet \n4.To print Book Enter \n5.To Exit')
    choice = int(input('Your choice.. '))
    
    if choice ==  1:
        searchNum(input('Please Enter the Phone Number: '))
    elif  choice == 2:
        searchName(input('Please Enter the Name: '))
    elif choice == 3:
        name, phone = input('Enter Name: '), input('Enter Phone: ')
        CorrPhone = checkNum(phone) #Check if number is valid 
        addCont(name, CorrPhone)
    elif choice == 4:
        print('------------------------------')
        print(Book)
        print('------------------------------')
    elif  choice == 5:
        print('------------------------------')
        print("Good Bye..")
        print('------------------------------')
        break
    
        
        
