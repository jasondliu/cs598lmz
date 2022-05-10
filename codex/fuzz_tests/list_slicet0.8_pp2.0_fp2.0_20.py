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
print repr(lst)
Copyright © 2000-2020 上海卡达网络科技有限公司 版权所有。违者必究。
"""
A = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

def fun(A):
    if not A:
        return []
    # print A
    # print A[0]
    # print A[len(A)-1]
    if A[0] != A[len(A)-1]:
        return []
    else:
        if len(A) == 2:
            return [A[0]]
        return [fun(A[1:len(A)-1])]


print fun(A)
