# Banking System
Python-based banking system that leverages OOD principles such as encapsulation and abstraction to create a user authentication mechanism that provides different functionalities based on role (admin or customer)

# Summary: 

Run file run.py it will call run_app() method of banking_system.py
when main() method call and will ask for password and username that are already saved in file user.txt
if user is admin it will give three option 
1. Customer Summary
2. Financial Forecast
3. Quit 
if admin enters 3 it will exit the program
if admin enters 1 it will show all details of users bank accounts and total balance of all accounts
if admin enters 2 it gives you forecast details of next year

if user is not admin:
there are options like
1- View account
2- View Summary
3 - Withdraw
4 - Deposit
5 - Exit

User class is for creating a user admin or a simple user
Customer class is inhriting user class and this is not for admin
Then there is Account class and there are two subtypes of Account class Saving account and current account

## Inputs:
input are list of users from text file (user.txt)

## Output:
output is when user withdraw or depost some money it will save in the same text file(user.txt)

# Running Project
"python run.py"
Enter in UserName and password for user roles outlined in user.txt
