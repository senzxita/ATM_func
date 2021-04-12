# Task on Zuri
# An ATM Mock Project
from random import randint
from datetime import datetime

# Date and Time
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print("The current date and time is", dt_string)

# Variables
userdb = ['Seyi', 'Mike', 'Love']
passdb = ['passwordSeyi', 'passwordMike', 'passwordLove']
accountdb = [1632763693, 7423509924, 8273178241]

# Function to Register a new user
def Register():
    Username = input("What is your name? \n")
    Password = input("Enter password: ")
    userdb.append(Username) 
    passdb.append(Password)
    print("\nSUCCESSFUL REGISTRATION")
    print("Welcome %s! \n" % Username)
    print("Account number is being generated...")
    account_no = randint(1000000000, 9999999999)
    accountdb.append(account_no)
    print("Your account number is %s \n" % account_no)
    

# Function for an existing user to login to the system   
def Login():
    Username = input("Enter your name: ")
    allowedUsers = userdb
    if(Username in allowedUsers):
        
        Password = input("Enter your password: ")
        userId = allowedUsers.index(Username)
        
        if(Password == passdb[userId]):
            print("SUCCESSFUL LOGIN \n")
            print('Welcome %s!' % Username)
            accountId = accountdb[userId]
            print("Your account number is %s \n" % accountId) 
            
        else:
            print('Password Incorrect, please try again')
            Login()

    else:
        print('Name not found, please try again')
        Login()

# The main function
def init():
    print("Welcome! are you a new user?")
    answer = input("Enter 'yes' or 'no': ")
    if answer == "yes":
        Register()
    else:
        Login()


    print('Available options:')
    print('Enter 1 for Withdrawal')
    print('Enter 2 for Cash Deposit')
    print('Enter 3 for Complaint\n')

    selectedOption = int(input('Please select an option: \n'))
        
    if(selectedOption == 1):
        print('you selected the withdrawal option')
        withdrawal = input("How much would you like to withdraw? ")
        print("take your cash of %s naira" % withdrawal)
        print("Would you like to recieve a receipt of your transaction?")
        receipt = input("Enter 'yes' for receipt, otherwise enter 'no':  ")

        if receipt == "yes":
            print("\nRECEIPT OF TRANSACTION")
            print("~~~~~~~~~~~~~~~~~~~~~~ \n")
            print("TYPE OF TRANSACTION: WITHDRAWAL")
            print("AMOUNT WITHDRAWN: %s naira" % withdrawal)
            print("DATE & TIME OF TRANSACTION: %s \n" % dt_string)
    
        else:
            print("NO RECEIPT GENERATED")


    elif(selectedOption == 2):
        print('you selected the deposit option')
        deposit = input("How much would you like to deposit? ")
        print('Your current balance is %s naira' % deposit)
        print("Would you like to recieve a receipt of your transaction?")
        receipt = input("Enter 'yes' for receipt, otherwise enter 'no': \n ")

        if receipt == "yes":
            print("\nRECEIPT OF TRANSACTION")
            print("~~~~~~~~~~~~~~~~~~~~~~ \n")
            print("TYPE OF TRANSACTION: DESPOSIT")
            print("AMOUNT WITHDRAWN: %s naira" % deposit)
            print("DATE & TIME OF TRANSACTION: %s \n" % dt_string)
    
        else:
            print("NO RECEIPT GENERATED")
             
    elif(selectedOption == 3):
        print('you selected the complaint option')
        complaint = input('What issue will you like to report? ')
        print("Thank you for contacting us")
        
    else:
        print('Invalid Option selected, please try again')
init()
   



