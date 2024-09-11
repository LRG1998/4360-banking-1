import json
from user import User
from account import Account



class Auth:
    def __init__(self):
        pass

    def login_again(self, username, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

        for user in users:
            if user['name'] == username:
                if user['password'] == password:
                    accounts = {}
                    for account in user['accounts']:
                        accounts[account['accountNumber']] = Account(account['balance'])
                    return User(user['name'], accounts)
                else:
                    print("name or password not found")
            else:
                print("name or password not found")
            
        return None
