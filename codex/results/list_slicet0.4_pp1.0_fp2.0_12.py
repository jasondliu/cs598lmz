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
print(keepali0e)

#Output:
#[<weakref at 0x00B4D3E0; dead>, <weakref at 0x00B4D3E0; dead>, []]
#[Finished in 0.1s]

#第一次调用callback函数，在callback函数中删除lst[0]，但是由于lst[0]是str()，所以删除不掉，所以lst的长度不变。
#第二次调用callback函数，由于lst[0]是str()，所以删除不掉，所以lst的长度不变。
#第三次调用callback函数，由于lst[0
