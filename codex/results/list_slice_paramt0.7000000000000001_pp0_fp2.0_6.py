import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst=[]
print(keepali0e[0]())

# with weakref.finalize(a,callback) as f:
#     print(f.alive)
# del a
# print(f.alive)

# test=weakref.finalize(a,callback)
# print(test.alive)
# del a
# print(test.alive)
