import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
ref1=weakref.ref(lst,callback)
del lst
keepalive.clear()
del keepalive
print(ref1())
print(lst)

#list
list1=['aaa','bbb','ccc']
print(list1[0])
print(list1[-1])
list1.append('ddd')
print(list1)
list1.insert(1,'eee')
print(list1)
list1.pop()
print(list1)
list1.pop(1)
print(list1)
list1[1]='zzz'
print(list1)
list1.append('aaa')
print(list1)
print(list1.count('aaa'))
print(list1.count('bbb'))
print(list1.index('aaa'))
list1.remove('aaa')
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.sort(reverse
