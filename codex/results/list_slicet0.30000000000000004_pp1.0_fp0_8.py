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

#练习：
#1.写一个类，实现一个方法，返回一个迭代器，迭代器返回一个数字，从1开始，每次迭代返回一个数字，返回的数字是上一次返回的数字加上1
#2.写一个类，实现一个方法，返回一个迭代器，迭代器返回一个数字，从1开始，每次迭代返回一个数字，返回的数字是上一
