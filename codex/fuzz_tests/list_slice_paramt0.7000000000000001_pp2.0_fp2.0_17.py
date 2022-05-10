import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a
del lst
print(keepali0e)
# gc.collect()
# print(keepali0e)

# def func(lst):
#     lst[0]="hello"
#     lst[1][0]=1
#
# lst=[0,{0:0}]
# lst=lst[:]
# func(lst)
# print(lst)
#
# n=1
# def f(n):
#     print(n)
#
# f(n)

# def get_text():
#     print(s)
#     return "hello"
#
#
# def func():
#     s="world"
#     get_text()
#
# func()

# class Foo(object):
#     def __getattr__(self, item):
#         print(item)
#     def __getattribute__(self, item):
#         print(item)
#        
