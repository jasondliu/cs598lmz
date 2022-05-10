import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
a.a=lst
lst[0]=a
weakref.ref(lst[0],callback)
print("End of test_gccrash1")

def test_gccrash2():
    # This is an infinite loop; it's only purpose is to crash the Python interpreter
    # See http://www.python.org/sf/583420
    class A(object):
        def __del__(self):
            self.b = self
    a = A()
    a.b = a
    print("End of test_gccrash2")

def test_gccrash3():
    # This is an infinite loop; it's only purpose is to crash the Python interpreter
    # See http://www.python.org/sf/583420
    class A(object):
        def __del__(self):
            self.b = self
    a = A()
    a.b = a
    print("End of test_gccrash3")

def test_g
