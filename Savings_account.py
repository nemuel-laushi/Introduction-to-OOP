from account import Account


class savingsAccount (Account):
    def __init__(self):
        super.__init__()
        
    def withdraw(self, amount):
        if amount < 2000:
            
         super().withdraw(amount)
         
        else:
            
            print("You can not withdraw above your limit")
               
savingsAccount = savingsAccount()
savingsAccount.withdraw(2000)
    