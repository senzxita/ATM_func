#This is a class

class Budget:
    """
    This is a class Budget
    """
    
    def __init__(self, depo, withd, trans):
        
        self.depo = depo
        self.withd = withd
        
        self.trans = trans
       

    

    def deposit(self):
        print("You have deposited %s naira" % self.depo)
        amount = self.depo

        
       

    def withdraw(self):
        
        print("You have withdrawn %s naira" % self.withd)
        amount = self.withd
        self.balance()
        
    
    



    def balance(self):
        bal = 0
        bal += self.depo
        bal -= self.withd
        print("Current balance is %s naira" % bal)
        print("Would you like to transfer or logout?")
        option = input("Enter 'transfer' for transfer else, 'logout': \n")
        
        if option == "transfer":
            self.transfer()
            
        elif option == "logout":
            print("You have ended all transactions")
            exit()
        else:
            print("Invalid option! try again")
            self.balance()
            


          

    def transfer(self):
        print("Where would you like to transfer to? \n")
        print("Enter 1, to transfer fund to clothing \n")
        print("Enter 2, to transfer fund to entertainment: \n")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            amount = int(input("Enter amount: "))
            print("You have successfully transferred %s naira" % amount)
            newbal = bal - amount
            self.balance()
        
        elif choice == 2:
            amount = int(input("Enter amount: "))
            
            print("You have successfully transferred %s naira" % amount)
            newbal = bal - amount
            self.balance()
        
        else:
            print("Enter a valid option")
            self.transfer()


        
       

food = Budget(2235, 243, 500)
food.deposit()
food.withdraw()
food.balance()
food.transfer()


clothing = Budget(1424, 241, 989)
clothing.deposit()
clothing.withdraw()
clothing.balance()
clothing.transfer()


entertainment = Budget(1424, 241, 989)
entertainment.deposit()
entertainment.withdraw()
entertainment.balance()
entertainment.transfer()


