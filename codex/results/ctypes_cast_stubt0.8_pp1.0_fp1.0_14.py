import ctypes
ctypes.cast(id(obj_1), ctypes.py_object).value

print('--------------------------------------')
print('Encapsulation:')

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, min_balance):
        BankAccount.__init__(self)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

a = BankAccount()
b = MinimumBalanceAccount(min_balance=20)

print('a.balance: ', a.deposit(50))
print('b.balance: ', b.deposit(50))

print('a.balance:
