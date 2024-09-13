from exceptions import InsufficientFundsException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount or amount >= 0: #added a check if user input was negative
            self.balance -= amount
            return self.balance
        else:
            raise InsufficientFundsException
    
    def deposit(self, amount):
        if amount >= 0:         #added a check if user input was negative
            self.balance += amount
            return self.balance
        else:
            print("Invalid Input")
