import types
types.ClassType

def new_init(self, name='', shares=0, price=0.0):
    self.name = name
    self.shares = shares
    self.price = price
    self.__total = 0.0

Stock.__init__ = new_init

s = Stock('ACME', 50, 91.1)
print(s.name)
print(s.shares)
print(s.price)
#print(s.__total)
