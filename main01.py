
class BankAccount:
    
    def __init__(self,owner):
        self.owner:str = owner
        self.balance: float = 0.0
        
    def deposit(self,amount:float):
        self.balance += amount
    
    def witdraf(self,amount:float):
        if self.balance > amount:
            self.balance -= amount
        
    def show_balance(self):
        
        print(f"{self.owner} Balansingiz: ${self.balance:,.2f}")
        
        
ac = BankAccount("nodirbek")

ac.deposit(100000000)
ac.witdraf(50000)


ac.show_balance()