import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return 'a' * n

    def write(self, b):
        raise NotImplementedError

print File().read(3)

"""


"""
#inheritance
class Parent():
    def show(self):
        print "Parent"
class Child(Parent):pass
Child().show()
"""

"""
#method overriding
class Parent():
    def show(self):
        print "Parent"
class Child(Parent):
    def show(self):
        print "Child"
Child().show()
"""


"""
#method overloading
class Arithmetic:
    def operation(self,a,b):
        return a+b
    def operation(self,a,b,c):
        return a+b+c
print Arithmetic().operation(1,2,3)
"""


"""
#magic methods
class MyClass:
    def __init__(self):
        print "Object created"
    def __del__(self):
        print "Object destroyed"

obj=MyClass()
del
