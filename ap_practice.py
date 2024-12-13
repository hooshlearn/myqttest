database = {}
Id = 1
def signup():
    global database
    global Id
    print("Enter your firstname : ")
    fname = input()
    print("Enter your lastname : ")
    lname = input()
    print("Enter your password : ")
    passw=input()
    database={Id:[fname,lname,passw]}
    Id += 1
    print(f"{fname} {lname} Thank you for signup ! your id is {Id}")
def login():
    global database
    print("Enter your id : ")
    uname = int(input())
    print("Enter your password :")
    passw=input()
    if uname in database.keys():
        if database[uname][2]==passw:
            print("LogedIn !")
            return 1

        else:
            print("Wrong pass !")
    else:
        print("Wrong ID !")

def menu():
    print("*******************")
    print("welcome to my app !")
    print("1. signup")
    print("2. Login")
    print("3. Exit")
    print("Enter a number :")
    
def runproj():
    while(True):
        menu()
        inp = input()
        print("*******************")
        if inp=='1':
            signup()
        
        elif inp=='2':
            login()

        elif inp=='3':
            print("Thanks for running our project !")
            break
        else:
            print("Wrong number ! Try Again !")


runproj()