import ctypes
ctypes.windll.user32.MessageBoxW(0, "alert", "alert", 0)

func = lambda *k:print(*k)
func(4,5,6)

# Building a class for a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.15
    def perimeter(self):
        return 2 * self.radius * 3.14
# Creating an object for the circle class
c = Circle(9)
print(c.radius) # 9
print(c.area()) # 254.35
print(c.perimeter()) # 56.52

# Creating a class to represent a bank account
class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Creating an object for bank account
a = BankAccount()
