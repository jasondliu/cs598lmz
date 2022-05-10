import types
types.MethodType?
obj = Spam()
obj.method
obj2 = Spam()
obj2.method
def newMethod(self, value):
    print('new method', value)
obj.method = types.MethodType(newMethod, obj)
obj.method(42)
obj2.method(1729)
Spam.classMethod(obj)
Spam.classMethod(obj2)
 
 
class Spam:
    count = 0
    def __init__(self):
        Spam.count += 1
    def printCount():
        print('Number of instances created:', Spam.count)
    printCount = staticmethod(printCount)
    def printHello():
        print('Hello world!')
    printHello = classmethod(printHello)
Spam.printCount()
a = Spam()
b = Spam()
c = Spam()
Spam.printCount()
Spam.printHello()
a.printHello()
 
 
 
 
class PropSquare:
    def __init__(self, start):
        self.value
