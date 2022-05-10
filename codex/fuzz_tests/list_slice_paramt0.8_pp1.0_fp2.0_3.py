import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
len(lst)

#1.知道命令行参数
# 参数解释
#nargs='*'
#表示从所有剩余参数读取值，存储到一个list中。
#nargs=1
# 表示从参数中读取一个值，例如：读取-f后面的字符。
#nargs='?'
# 表示从参数中读取0或一个值，默认值default='XXX'。例如：读取-f后面的字符，如果-f后面没有字符则
