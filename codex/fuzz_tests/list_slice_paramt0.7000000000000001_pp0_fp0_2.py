import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
while lst:
    pass
import binascii
def my_decode(x,encoding='utf-8'):
    return x.decode(encoding)
def my_encode(x,encoding='utf-8'):
    return x.encode(encoding)
def my_int(x,base=10):
    return int(x,base)
def my_hex(x):
    return hex(x)
def my_bin(x):
    return bin(x)
def my_oct(x):
    return oct(x)
def my_chr(x):
    return chr(x)
def my_ord(x):
    return ord(x)
def my_eval(x):
    return eval(x)
def my_compile(x,mode='eval'):
    return compile(x,mode)
def my_exec(x):
    return exec(x)
def my_execfile(x):
    return execfile(x)
def my_input(x):
