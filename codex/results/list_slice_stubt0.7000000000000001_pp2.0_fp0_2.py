import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalivr.append(weakref.ref(a,callback))
#import gc
#gc.collect()
print lst
del a

# import weakref
# class A(object):
#     def __init__(self):
#        print 'init'
#     def __del__(self):
#         print 'del'
# def callback(x):
#     print 'called back'
# keepalive=[]
# a=A()
# keepalive.append(weakref.ref(a,callback))
# del a
# import gc
# gc.collect()
# A()

# import weakref
# class A(object):
#     def __init__(self):
#        print 'init'
#     def __del__(self):
#         print 'del'
# def callback(x):
#     print 'called back'
# keepalive=[]
# a=A()
# keepalive.append(weakref.ref(a,callback))
# keepalive.append(
