import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
print(lst[0])
del keepalive
print(lst)
print(lst[0])

#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

#示例 1:

#输入: "abcabcbb"
#输出: 3 
#解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#示例 2:

#输入: "bbbbb"
#输出: 1
#解释:
