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
print(lst)
#print(keepali0e)

#3.3.3
#给定一个字符串，找出它的所有排列组合
def permutation(s):
    if len(s)==1:
        return s
    res=[]
    for i,c in enumerate(s):
        for cc in permutation(s[:i]+s[i+1:]):
            res.append(c+cc)
    return res
print(permutation('abc'))

#3.3.4
#给定一个字符串，找出它的所有子串
def sub_strings(s):
    res=[]
    for i in range(len(s)):
        for j in range(i,len(s)):
            res.append(s[i:j+1])
    return res
print(sub_strings('abc'))

