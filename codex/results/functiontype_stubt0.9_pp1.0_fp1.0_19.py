from types import FunctionType
a = (x for x in [1])
def b(a):
	b = 1
	return a(b)
def c(cc):
	return cc == 1
c(5)
if type(c) == FunctionType:
	print b(c)

#>>> b(c)
#True

def a(cc = 1):
	return cc

#equals...

class a():
    def __init__(self, cc = 1):
        self.cc = cc
    def __call__(self, cc = 1):
        if hasattr(self, 'cc'):
        	return self.cc
        else:
        	return cc


#>>> c = a()
#>>> c()
#1
#>>> c(5)
#5


#test...
class a(): c = 1
b = a()
print b.c
if hasattr(b, 'c'):
	print 'yes'
#>>>b.c
#1
#yes
