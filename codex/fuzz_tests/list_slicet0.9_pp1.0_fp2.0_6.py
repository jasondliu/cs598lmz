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
if __name__ == '__main__':
    from sys import stdout
    from traceback import print_exc
    try:
        startmarker()
    except RuntimeError as x:
        print_exc(file=stdout)
        print('OK')
    else:
        print(keepalive)
        print('ERROR')
