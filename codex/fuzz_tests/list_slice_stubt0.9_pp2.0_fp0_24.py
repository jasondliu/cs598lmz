import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
d=weakref.WeakKeyDictionary()
d[a]=1
wr=weakref.ref(a,callback)

print(type(wr))
'''
while keepali0e:
    del keepali0e[0]
    d={}
    d[1]=1
    print(d)
'''
if __name__ == '__main__':
    pass
