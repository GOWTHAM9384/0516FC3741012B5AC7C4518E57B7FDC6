class BankAccount:
    
    def __init__(self, account_number, account_holder_name, account_balance):
       
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = account_balance

    
    def deposit(self, amount):

        if amount > 0:
            
            self._account_balance += amount
            
            print(f"Deposited {amount} to the account {self._account_holder_name} {self._account_number}.")
        else:
          
            print("Invalid amount. Please enter a positive value.")

   
    def withdraw(self, amount):
       
        if amount > 0 and amount <= self._account_balance:
         
            self._account_balance -= amount
           
            print(f"Withdrew {amount} from the account {self._account_holder_name} {self._account_number}.")
        else:
            
            print("Invalid amount. Please enter a positive value that is less than or equal to the current balance.")

   
    def display_balance(self):
        
        print(f"The balance of the account {self._account_number} is {self._account_balance:.2f}.")

my_account = BankAccount(9826644774747,"gowtham", 10000)

my_account.deposit(1000)
my_account.deposit(5000)

my_account.withdraw(600)
my_account.withdraw(300)

my_account.display_balance()
