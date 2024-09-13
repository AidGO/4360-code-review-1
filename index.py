import os
from message import Message
from interface import UserInterface
from user import User
from account import Account
from auth import Auth


def main():
    message = Message()
    ui = UserInterface()
    auth = Auth()
    
    #authenticate user
    loginAttempts = 0   #changed to from login_attempts to loginAttempts for consistency
    failedAttempt = False
    while loginAttempts < 3:
        os.system('cls')
        if failedAttempt:
            message.print("please try again")
        message.print("Welcome to the bank of Py!")
        message.print("please login to continue.")

        userName = input("Username: ")
        password = input("Password: ")   #inconsistent message, no colon or capitalization. Changed from "password" to "Password: "

        user = auth.login(userName, password)
        if not user:
            loginAttempts += 1
            failedAttempt = True
        else:
            break

    #register UI
    if user != None: #CRASHES WHEN MAX ATTEMPTS IS REACHED BECAUSE USER IS NONE TYPE, fixed with this line
        ui.register_command("deposit", user.deposit, "deposit [accountNumber] [amount] - deposit an amount into an account\n")    #No indents, makes the directions harder to read, added some
        ui.register_command("withdraw", user.withdraw, "withdraw [accountNumber] [amount] - withdraw an amount from an account\n")
        ui.register_command("transfer", user.transfer, " transfer [fromAccountNumber] [toAccountNumber] [amount] - transfer an amount from one account to another account\n")
    

        #Main Loop
        while True:
            os.system('cls')
            message.print("What can we do for you today?")
            user.show_accounts()
            ui.show_commands()
            userInputs = input().lower().split(" ") #changed user_inputs to userInputs for consistency

            #exit check
            if(userInputs[0] == "exit"):
                print("Good bye")
                break

            print(userInputs)
            ui.execute_command(userInputs[0], userInputs[1:])
        



if __name__ == "__main__":
    main()
   

