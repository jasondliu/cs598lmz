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

#2.给定一个字符串，如何判断其中是否包含重复的字符？
#方法一：
def is_duplicated(s):
    return len(set(s)) != len(s)
#方法二：
def is_duplicated(s):
    return len(s) != len(set(s))
#方法三：
def is_duplicated(s):
    return len(s) > len(set(s))
#方法四：
def is_duplicated(s):
    return len(s) != len(frozenset(s))
#方法五：
def is_duplicated(s):
    return len(frozenset(s)) != len(s)
#方法六：
def is_duplicated(s):
