import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print(keepali0e,lst)
a.a=weakref.ref(lst,callback)
print(keepali0e,lst)

'''
[<weakref at 0x7fdc34010548; to 'A' at 0x7fdc340ec198>] ['']
[<weakref at 0x7fdc34010548; to 'A' at 0x7fdc340ec198>] []
'''

# 访问一个对象的弱引用:

'''
>>> import weakref
>>> class C(object): pass
...
>>> c = C()
>>> ref = weakref.ref(c)
>>> ref
<weakref at 0x1097be9e8; to 'C' at 0x1097be8d0>
>>> ref() is c
True
>>> obj = ref()
>>> obj is c
True
'''

#weakref.ref 的基类是 weakref.ProxyType

# 无法
