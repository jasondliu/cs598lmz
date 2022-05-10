import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
lst
del lst

# lst=[str()]
# lst
# lst.append('a')
# lst
# lst.append(1)
# lst
# lst.append([1,2,3])
# lst
# lst.pop()
# lst
# lst.pop()
# lst
# lst.pop()
# lst

# a='a'
# b='b'
# c='c'
# lst=[a,b,c]
# lst
# lst.remove('b')
# lst
# lst.remove('a')
# lst
# lst.remove('c')
# lst

# lst.insert(0,'a')
# lst
# lst.insert(0,'b')
# lst
# lst.insert(0,'c')
# lst
# lst.remove('a
