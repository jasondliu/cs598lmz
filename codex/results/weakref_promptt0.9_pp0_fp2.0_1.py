import weakref
# Test weakref.ref List
class A:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    def fun1(self):
        print 'fun1:',self.value

# a = A(10)
a = weakref.ref(A(10))
print a
print a.value
