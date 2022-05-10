import types
# Test types.FunctionType equivalent arguments
def f(a, b, c): return a + b

#<-----------------
def f2(a, b, c):
        print a, b, c

def f3(a, b, c):
    c.baz_qux()

def f4(a, b, c):
    pass
#----------------->

print equals(f, f, (), "")
#Test error conditions
try:
        equals(f, f2, (1,2,3), "")
except AssertionError, e:
        print e

try:
        equals(f, f3, (1,2,3), "")
except AssertionError, e:
        print e

try:
        equals(f, f4, (1,2,3), "")
except AssertionError, e:
        print e

# Another test: what about equality of function objects
# that have __cmp__'s
def fc1(): pass
def fc2(): pass
def fc3(arg): pass
def fc3(arg):
