import types
types.MethodType(f,None,Spam)

class Spam:
    data=1
    def meth(self):
        pass

x=Spam()
x.data
x.meth()

hasattr(x,'data')
hasattr(x,'meth')
hasattr(x,'ham')

getattr(x,'meth')

try:
    getattr(x,'ham')
except AttributeError:
    print("no ham")

getattr(x,'ham','nope')

setattr(x,'ham','eggs')
x.ham

class Person:
    def __init__(self,name,job,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))

bob=Person('Bob Smith','dev',10000)
sue=Person('Sue Jones','hd
