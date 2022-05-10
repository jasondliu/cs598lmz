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
# test whether getstrongrefs can generate references to the list and its contents
keepalive=[]
lst=[str(),0]
keepalive.append(lst)
keepalive.append(lst[:])
keepalive.append(lst[0])
keepalive.append(lst[1])
del keepalive
if(getstrongrefs(lst)!=[]):raise test_support.TestFailed,"""\
getstrongrefs omits an object still strongly referenced by the
original argument
"""
# make sure getweakrefs returns something reasonable
if(getweakrefs(lst)!=[]):raise test_support.TestFailed,"""\
getweakrefs of a live object without weak references returns non-empty list
"""
# test whether getweakrefs can generate references to the list and its
# contents
def del_lst(x):del lst[0]
def del_lst_x(x):del lst[0:1]
def empty(x):pass
lst=[str(),0]
keepalive=[l
