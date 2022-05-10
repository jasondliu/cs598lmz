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



# http://paste.ubuntu.com/4772461/

# Python 2.6.8 (default, May 11 2013, 19:18:21) 
# [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> while True:
# ...  class A(object):pass
# ...  class B(object):pass
# ...

# Crashes Python 2.6.8 and 3.2.3 (obviously)


# Python 2.6.8 (default, May 11 2013, 19:18:21) 
# [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> while True:
# ...  class A(object):pass
# ...  class B(object):pass
#  File "<stdin>",
