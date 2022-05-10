import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
print lst

#编写一个函数，它接受一个整数n和一个可选的整数基数k，返回一个长度为n的字符串表示形式。
#默认基数为10，如果指定了基数，则基数必须介于2和36之间。
#返回的字符串中的字母必须大写，如果基数小于10，则数字必须使用0-
