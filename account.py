class Account:
    def __init__(self):
        self.balance = 10000
        self.interest_rate = 5
        self.__id_number = 10566788
        print("starting balance is ", self.balance)
        
    def get_interest_rate(self):
        return self.get_interest_rate
        
    def get_id_number(self):
        return self.__id_number
    
    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number
        return self.set_id_number
        
        
    def deposit(self, amount):
            self.balance = amount + self.balance
            print("new: ", self.balance)
        
    def withdraw(self, amount):
           if amount < 2000:
               super().withdraw(amount)
           else:
               print("You can not withdraw above your limit")
            
Account=Account()
Account.deposit(2000)
            
       