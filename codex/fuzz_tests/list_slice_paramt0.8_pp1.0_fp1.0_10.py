import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
lst,len(lst)

def func():pass
func()
func.func_code=0
def func():pass
func.__code__=0

def func(a):return a
func(1)
func.__code__=0

def func():pass
def func():pass
def func():pass
del func

def func():pass
func.func_code=0

def func(a):return a
func.__code__.co_varnames= 42
func(1)

del __builtins__.open

try:
    open()
    print('FAIL, open() did not raise NameError')
except NameError,e:
    print('PASS')
except Exception:
    print('FAIL, open() raised unexpected exception')

try:
    open()
    print('FAIL, open() did not raise NameError')
except NameError,e:
    print('PASS')
except Exception:
    print('FAIL, open() raised unexpected exception')

try:

