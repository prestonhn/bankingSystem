

class User:
    def __init__(self, username, password,user_type):
        self.username = username
        self.password = password
        self.user_type = user_type
class Customer(User):
    def __init__(self,username,password,user_type,address,current_account,saving_accounts=[]):
        super().__init__(username, password,user_type)
        self.address = address
        self.current_account = current_account
        self.saving_accounts = saving_accounts

class Account():
    def __init__(self,account_type,balance):
        self.account_type = account_type
        self.balance = balance
class CurrentAccount(Account):
    def __init__(self,overdraft_limit,account_type,balance):
        super().__init__(account_type,balance)
        self.overdraft_limit =  overdraft_limit

class SavingAccount(Account):
    def __init__(self,interest_rate,account_type,balance):
        super().__init__(account_type,balance)
        self.interest_rate = interest_rate

class BankingSystem:
    def __init__(self):
        # Do not add any parameter to this method.
        # Delete "pass" after adding code into this method.
        self.users = []
        #admin
        self.users.insert(0,User("Arthur","123","admin"))
        c1_current_account = CurrentAccount(100,"Current account",1000)
        #user 1
        self.users.insert(1,Customer("Boris","ABC","customer","10 London Road",c1_current_account))
        #user 2
        c2_current_account = CurrentAccount(100,"Current account",1000)
        c2_saving_accounts = []
        c2_saving_accounts.append(SavingAccount("2.99%","Saving account",4000)) 
        self.users.insert(2,Customer("Chloe","1+x","customer","99 Queens Road",c2_current_account,c2_saving_accounts))
        #user 4 
        c3_current_account = CurrentAccount(0,"None",0)
        c3_saving_accounts = []
        c3_saving_accounts.insert(0,SavingAccount("0.99%","Saving account",200)) 
        c3_saving_accounts.insert(1,SavingAccount("4.99%","Saving account",5000)) 
        self.users.insert(3,Customer("David","aBC","customer","2 Birmingham Street",c3_current_account,c3_saving_accounts))

    def run_app(self):
        print("Your banking system should run by calling this method.")
        username = input("Enter username:")
        password = input("Enter Password:")
        count = 0
        for i in range(len(self.users)):
            if(self.users[i].username == username and self.users[i].password==password):
                if(self.users[i].user_type == "admin"):
                    while(True):
                        print("Please select an option:")
                        print("  1 - Customer Summary")
                        print("  2 - Financial Forecast")
                        print("  3 - Quit")
                        try:
                            option = int(input("Enter a number to select your option:"))
                            if(option<1 or option > 3):
                                print("Invalid Input")
                                print(" ")
                            elif(option == 3):
                                print("Exit")
                                print(" ")
                                break
                            elif(option == 1):
                                print("List all customers information:")
                                for u in range(1,len(self.users)):
                                    print("Name: ",self.users[u].username)
                                    print("Address: ",self.users[u].address)
                                    print("Accounts Information:")
                                    if(self.users[u].current_account.account_type != "None"):
                                        print("Account Type: ",self.users[u].current_account.account_type)
                                        print("Balance: €",self.users[u].current_account.balance)
                                        print("Overdraft limit: ",self.users[u].current_account.overdraft_limit)
                                    for sa in range(len(self.users[u].saving_accounts)):
                                        print("Account Type: ",self.users[u].saving_accounts[sa].account_type)
                                        print("Balance: €",self.users[u].saving_accounts[sa].balance)
                                        print("Interest Rate: ",self.users[u].saving_accounts[sa].interest_rate)
                                    print(" ")
                            elif(option == 2):
                                print("--Financial Forecast--")
                                for u in range(1,len(self.users)):
                                    total_balance = 0
                                    print("Name: ",self.users[u].username)
                                    if(self.users[u].current_account.account_type != "None"):
                                        print("No of bank accounts: ",len(self.users[u].saving_accounts)+1)
                                        total_balance =  total_balance + self.users[u].current_account.balance
                                    elif(self.users[u].current_account.account_type == "None"):
                                        print("No of bank accounts: ",len(self.users[u].saving_accounts))
                                    for sa in range(0,len(self.users[u].saving_accounts)):
                                        if(len(self.users[u].saving_accounts)!=0):
                                            total_balance = total_balance+self.users[u].saving_accounts[sa].balance
                                        else:
                                            break
                                    print("Total Balance: €",total_balance)
                                    print("Forecast of total money after a year: €",total_balance*12)
                                    print(" ")
                                print(" ")
                        except Exception as e:
                            print("Invalid Input")
                            print(e)
                            print(" ")

                else:
                    user = self.users[i]
                    while(True):
                        print("Please select an option:")
                        print("  1 - View account")
                        print("  2 - View summary")
                        print("  3 - Quit")
                        try:
                            option = int(input("Enter a number to select an option:"))
                        except:
                            print("Invalid Input")
                            print(" ")
                        if(option == 3):
                            print("Exit")
                            break
                        elif(option == 1):
                            while(True):
                                print(" ")
                                print("--Account list--")
                                print("Please select an option:")
                                accounts_count = 1
                                if(user.current_account.account_type != "None"):
                                    print(f"  {accounts_count} - Current Account: €{user.current_account.balance}")
                                    accounts_count =  accounts_count + 1
                                if(len(user.saving_accounts)!=0):
                                    for j in range(len(user.saving_accounts)):
                                        print(f"  {accounts_count} - Saving Account: €{user.saving_accounts[j].balance}")
                                        accounts_count = accounts_count + 1
                                try:
                                    account_option = int(input("Enter a number to select your option:"))
                                except:
                                    print("Invalid Input")
                                    print(" ")
                                    break
                                if(account_option<1 or account_option > accounts_count-1):
                                    print("Invalid Input")
                                    print(" ")
                                    break
                                else:
                                    if(account_option == 1 and user.current_account.account_type != "None"):
                                        print(" ")
                                        print(f"You selected {account_option} - Current Account: €{user.current_account.balance}")
                                        print("Please select an option:")
                                        print("1 - Deposit ")
                                        print("2 - Withdraw ")
                                        print("3 - Go back ")
                                        try:
                                            money_option = int(input("Enter a number to select your option: "))
                                        except:
                                            print("Invalid Input")
                                            print(" ")
                                            
                                        if(money_option<1 or money_option > 3):
                                            print("Invalid Input")
                                        elif(money_option == 1):
                                            deposit_amount = int(input("Enter Amount you want to deposit: "))
                                            user.current_account.balance = user.current_account.balance + deposit_amount
                                            print("Deposit Done")
                                        elif(money_option == 2):
                                            withdraw_money = int(input("Enter Amount you want to withdraw: "))
                                            if(withdraw_money < 0 or withdraw_money>user.current_account.balance):
                                                print("Insuffichent balance")
                                            else:
                                                user.current_account.balance = user.current_account.balance - withdraw_money
                                                print("Withdrawl Done")
                                        elif(money_option == 3):
                                            pass
                                    elif(account_option != 1 and user.current_account.account_type != "None"):
                                        print(f"You selected {account_option} - Saving Account: €{user.saving_accounts[account_option-2].balance}")
                                        print("Please select an option:")
                                        print("1 - Deposit ")
                                        print("2 - Withdraw ")
                                        print("3 - Go back ")
                                        try:
                                            money_option = int(input("Enter a number to select your option: "))
                                        except: 
                                            print("Invalid Input")
                                        if(money_option<1 or money_option > 3):
                                            print("Invalid Input")
                                        elif(money_option == 1):
                                            deposit_amount = int(input("Enter Amount you want to deposit: "))
                                            user.saving_accounts[account_option-2].balance = user.saving_accounts[account_option-2].balance + deposit_amount
                                            print("Deposit Done")
                                        elif(money_option == 2):
                                            withdraw_money = int(input("Enter Amount you want to withdraw: "))
                                            if(withdraw_money < 0 or withdraw_money>user.saving_accounts[account_option-2].balance):
                                                print("Insuffichent balance")
                                            else:
                                                user.saving_accounts[account_option-2].balance = user.saving_accounts[account_option-2].balance - withdraw_money
                                                print("Withdrawl Done")
                                        elif(money_option == 3):
                                            pass
                                    else:
                                        print(f"You selected {account_option} - Saving Account: €{user.saving_accounts[account_option-1].balance}")
                                        print("Please select an option:")
                                        print("1 - Deposit ")
                                        print("2 - Withdraw ")
                                        print("3 - Go back ")
                                        try:
                                            money_option = int(input("Enter a number to select your option: "))
                                        except:
                                            print("Invalid Input")
                                        if(money_option<1 or money_option > 3):
                                            print("Invalid Input")
                                        elif(money_option == 1):
                                            deposit_amount = int(input("Enter Amount you want to deposit: "))
                                            user.saving_accounts[account_option-1].balance = user.saving_accounts[account_option-1].balance + deposit_amount
                                            print("Deposit Done")
                                        elif(money_option == 2):
                                            withdraw_money = int(input("Enter Amount you want to withdraw: "))
                                            if(withdraw_money < 0 or withdraw_money>user.saving_accounts[account_option-1].balance):
                                                print("Insuffichent balance")
                                            else:
                                                user.saving_accounts[account_option-1].balance = user.saving_accounts[account_option-1].balance - withdraw_money
                                                print("Withdrawl Done")
                                        elif(money_option == 3):
                                            pass
                                


                        elif(option == 2):
                            if(user.current_account.account_type != "None"):
                                print("Your Total no of bank accounts are: ",len(user.saving_accounts)+1)
                            else:
                                print("Your Total no of bank accounts are: ",len(user.saving_accounts))
                            total_balance = user.current_account.balance
                            for k in range(len(user.saving_accounts)):
                                total_balance = total_balance + user.saving_accounts[k].balance
                            print("Total balance of all accounts: ",total_balance)
                            print("Address: ",user.address)
                            print(" ")
                        else:
                            print("Please Select Valid Option:")
                break
            count = count+1
        if(count == len(self.users)):
            print("No User Found")
        
        