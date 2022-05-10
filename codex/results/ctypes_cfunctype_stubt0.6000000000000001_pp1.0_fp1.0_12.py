import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2():
    return 2

class X(object):
    def __init__(self):
        self.fun = fun
        self.fun2 = fun2

class Y(X):
    pass

x = X()
y = Y()

print x.fun() #1
print y.fun() #1
print y.fun2() #2
print y.fun == x.fun #True
print y.fun2 == x.fun2 #False

#-------------------------
#-------------------------

#def fun3():
#    return 3

#y.fun3 = fun3
#print y.fun3() #3
#print y.fun3 == x.fun3 #False
