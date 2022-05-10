import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print lst
print keepali0e

#正则表达式
import re
p=re.compile('[a-z]+')
m=p.match("tempo")
print m.group()
print m.start()
print m.end()
print m.span()

#测试一个正则表达式是否匹配一个字符串
import re
p=re.compile('[a-z]+')
print p.match('tempo')
print p.match('temp')
print bool(p.match('temp'))

#搜索字符串
import re
p=re.compile('[a-z]+')
m=p.search(':::message')
print m.group()
print m.start()
print m.end()
print m.span()

#搜索所有
