import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
weakref.ref(a,callback)
"""

#test_repr_builtin
test_inc_repr_builtin="""
def f():pass
for i in xrange(100):
    repr(f)

"""

#test_list_comprehensions
test_inc_list_comprehensions="""
def a():
    return [1,2,3,4,5]

def b():
    return [a()[i] for i in range(5)]

def c():
    return [a()[i] for i in range(5) if i>2]

def d():
    return [a()[i] for i in range(5) if i>3]

def e():
    return [a()[i] for i in range(5) if i>4]
"""

#test_nested_scopes
test_inc_nested_scopes="""
def a():pass
def b():return a()


