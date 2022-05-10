import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
''')

def test_func2(space, w):
    space.execute("""
def func(a,b):
    return a+b
result = func(2, 3)
""")
    assert space.int_w(space.getattr(space.getitem(space.builtin.w_locals,
                                                   space.newtext('result')),
                                     space.newtext('__class__'))) is space.w_int
    assert space.unwrap(space.getitem(space.builtin.w_locals,
                                      space.newtext('result'))) == 5

def test_globals(space, w):
    space.execute("""
global a
a = 5
def func():
    global a
    a = 10
func()
""")
    a = space.getitem(space.builtin.w_globals, space.newtext('a'))
    assert space.unwrap(a) == 10

def test_simple_tuple(space, w):
    space.execute("a = 1, 2
