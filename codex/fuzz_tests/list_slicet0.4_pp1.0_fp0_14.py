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

#更新字典
def update(d,u):
    for k,v in u.items():
        if isinstance(v,Mapping):
            r=update(d.get(k,{}),v)
            d[k]=r
        else:
            d[k]=u[k]
    return d

#排序字典
from operator import itemgetter
x={1:2,3:4,4:3,2:1,0:0}
print(sorted(x.items(),key=itemgetter(1)))

#链式比较
a=2
b=3
print(1<a<3)
print(1<a<b<5)

#列表推导式
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([[row[i] for row in matrix] for i in range(
