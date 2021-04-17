class Budget:
    #first instantiating object of the class
    def __init__(self, name):
        self.name = name
        self.ledger = list()



    #object method for depositing which accept two main parameter, amount and description
    def deposit(self, amount, description=""):
            self.ledger.append({"amount": amount, "description": description})


    #object method for withdrawing which amount and description as paramenter
    def withdraw(self, amount, description=""):

        #if statement/condition used to check if there is funds or not.
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False


    #object method getting the category balance. it returns the actual/current balance/funds.
    def category_balance(self):
        total_cash = 0

        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash

    #object method for for transfer
    def transfer(self, amount, category):

        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        return False
    

    #object method used to check for funds
    def check_funds(self, amount):
        #if statement to check current balance is greater than the initial amount
        if(self.category_balance() >= amount):
            return True
        return False





#testing values
print("**********Food Analysis for deposit, withdraw, transfer, checking of balance****")
food = Budget("Food")
food.deposit(2000, "First Deposit")
food.withdraw(300, "Milk")
food.withdraw(200, "drinks")
print(food.category_balance())

print("****Clothing Analysis for deposit, withdraw, transfer, checking of balance *****")
clothing = Budget("clothing")
clothing.deposit(5000, "Second Deposit")
clothing.withdraw(2500, "For a pair of pants and shirts")
food.transfer(500, clothing)
print(clothing.category_balance())


print("****Entertainment Analysis for deposit, withdraw, transfer, checking of balance *****")
entertainment = Budget("entertainment")
entertainment.deposit(7000, "Second Deposit")
entertainment.withdraw(1500, "For a music album")
clothing.transfer(700, entertainment)
print(entertainment.category_balance())

