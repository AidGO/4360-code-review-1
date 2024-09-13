import json
from user import User
from account import Account
from message import Message

message = Message()

class Auth:
    def __init__(self):
        pass

    def read_from_db(self):
        with open('db.json', 'r') as file:     #added a fuction to ease the load of the login function
            return json.load(file)['users']
    
    def login(self, username, password):     #hard to read (too many accounts)
        users = self.read_from_db()
        for user in users:
            if user['name'] == username and user['password'] == password:  #deleted an if statement that wasn't needed for readablility
                accounts = {}
                for account in user['accounts']:
                    accounts[account['accountNumber']] = Account(account['balance'])
                return User(user['name'], accounts)
            else:
                message.print("name or password not found")   #Un-needed print message, gets cleared by os.system('cls')
            
        return None
