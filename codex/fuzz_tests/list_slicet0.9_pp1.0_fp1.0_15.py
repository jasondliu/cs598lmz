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
print len(keepali0e)
keepali0e.append([])
keepali0e.pop()
print keepali0e
'''
r = t.split()
print(r)
lines = []
i = 0

for line in r:

    if line.strip():  # 去掉空白
        # split() 預設是以空白字元切割
        # 以 # 為例，預設會被視為欄位分隔符號，因此會被忽略，因此輸出只有兩個欄位
        # col1, col2 = line.split()
        col1, col2 = line.split(',')
        # print(col1)  # 印出第一個欄位
        #
