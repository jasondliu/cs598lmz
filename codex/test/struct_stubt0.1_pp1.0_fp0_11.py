from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用类来创建具有特定行为的实例
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

s = Stock('ACME', 50, 91.1)
s.cost()

# 可以使用类来创建具有特定行为的实例
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
