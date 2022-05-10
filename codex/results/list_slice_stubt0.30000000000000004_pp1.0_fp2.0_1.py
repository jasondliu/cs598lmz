import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
keepalive.append(lst)
weakref.ref(a,callback)
del a
del keepalive
del lst

#编写一个函数，返回一个函数，返回的函数可以记住第一次调用时传递给它的参数
def make_adder(n):
    def adder(x):
        return x+n
    return adder
add5=make_adder(5)
add5(2)

#编写一个函数，返回一个函数，返回的函数可以记住第一次调用时传递给它的参数
def make_adder(n):

