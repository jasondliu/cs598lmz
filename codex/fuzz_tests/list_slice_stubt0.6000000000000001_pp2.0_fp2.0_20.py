import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(weakref.ref(a,callback))
keepalive.append(lst)

#检查一个对象的弱引用
import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
b.a is a
True
a_wr=weakref.ref(a)
b_wr=weakref.ref(b)
b_wr()is a_wr()
True

#在python中实现一个可以接受任意参数的函数
def log(message,*values):
    if not values:
        print(message)
    else:
        values_str=','.join(str(x) for x in values)
        print('%s:%s'%(message,values_str))
log('My numbers are',1,2)
log('Hi there')
My numbers are:
