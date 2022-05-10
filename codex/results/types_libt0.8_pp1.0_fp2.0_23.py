import types
types.MethodType(func, list)

l = [1,2,3]

l.has_key = types.MethodType(func, l)
print l.has_key(2)

##-----------------------------------------------------------------------------

## 4.2.2 Class

class A(object):
    pass

a = A()
print type(a)  # <type 'instance'>
print type(A)  # <type 'classobj'>
print type(type)  # <type 'type'>  type is a class and type(type) is 'type'

class A(object):
    def __init__(self, msg):
        self.msg = msg
    def __repr__(self):
        return self.msg

a = A("Hello")
print a

##-----------------------------------------------------------------------------

## 4.2.3 Inheriting

class A(object):
    def __init__(self, msg, msg2):
        self.msg = msg
        self.msg2 = msg2
    def __repr__(self):
        return self.msg
    def print_msg
