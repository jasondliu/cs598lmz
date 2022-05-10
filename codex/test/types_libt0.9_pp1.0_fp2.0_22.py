import types
types.ClassType, types.TypeType

#these are examples of objects that dont exist directly
class MyClass: pass
X = MyClass
X

def UpperAttr(self, name):
    return getattr(self, name).upper()

#you can add instance attributes
#even to types
#because types are just classes
#that create other classes
for eachclass in [str, list, set]:
    eachclass.title = UpperAttr

['hello', 'world'].title()

#you can even add instance methods
#again ... types are just classes
def title(self):
    return self.title()
str.title = title

'hello'.title()

#that was interesting, types are just classes
#so what is a class?
#is it actually a type?
myclass = MyClass
myclass()

#a class is an object that creates instance objects
#it is an object that makes other objects
#it is a factory object
#these are the properties of a type class

a = 8
b = 8

#the number 8 is the same number in both cases
