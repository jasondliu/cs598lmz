import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
del a
del lst
keepali0e[0].c=None
keepali0e[1].append(weakref.ref(keepali0e[1][0],callback))
'''
def test1():
    keepalive=[str()]
    lst=[str()]
    try:
        keepalive.append(lst)
        lst.append(weakref.ref(lst[0],lambda x:del lst[0]))
    except RuntimeError as e:
        print(e)

'''
import sys
import gc
gc.disable()
class A(object):
    def __del__(self):
        print('del')
        sys.exit(0)
a=A()
del a
'''
def test2():
    import sys
    import gc
    gc.disable()
    class A(object):
        def __del__(self):
            print('del')
            sys.exit(0)
   
