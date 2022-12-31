import getpass
class Bank:
    
    
    def __init__(self,initial_amount=0.00):
        self.balance = initial_amount
        
    def log_transaction(self, transaction_string):
        with open("transaction.txt","a") as file:
            file.write(f"{transaction_string} \t\t\t Balance: {self.balance}\n")
        
    # withdraw
    def withdrawal(self,amount):
        
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance-amount
            self.log_transaction(f"Withdrew {amount}")
    # # Deposit
    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance+amount
            self.log_transaction(f"Deposited {amount}")

account = Bank(100.00)
while True:
    print("Insert ATM Card: ")
    pin = getpass.getpass(prompt="Enter your 4 digits PIN: ")
    if pin.isnumeric() and pin.isdigit() :
        try:
            action  = input("Enter the type of Transaction \n 1.withdrawal 2.deposit  \n: ")
        except KeyboardInterrupt:
            print("\nLeaving the ATM.....")
            break
        if action in ["withdrawal","deposit"]:
            if action == "withdrawal":
                amount = float(input("Enter the withdrawal amount: "))
                if amount > account.balance:
                    print("Insufficient balance...") 
                else:
                    account.withdrawal(amount)
            else:
                amount = input("Enter the deposit amount: ")
                account.deposit(amount)
            print("Your balance is",account.balance)    
        else:
            print("That is not a valid action.Try again.")
            
            
        exit=input("If You to exit [y] | [n]: ")
        if exit == "y":
            print("Leaving the ATM.....")
            break     
        
        
        
        
        
              
