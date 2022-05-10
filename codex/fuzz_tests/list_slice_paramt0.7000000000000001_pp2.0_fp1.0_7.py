import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
print(lst)

# 执行结果：
# ['a']
# ['', '']

# 答案:
# ['a']
# ['', '']

# 解析：
# del a
# 这一行调用del时，a被销毁，回调函数callback被调用，实现了del lst[0]，
# 所以最后输出为['','','']


# 6、
# 下面的程序输出什么？

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref
