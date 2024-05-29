from account import Account
class CurrentAccount(Account):
    
    def __init__(self):
        super().__init__()
        
currentAccount = CurrentAccount()

currentAccount.deposit(2000)
        
        
        
    
            