import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
print(keepali0e[0]() is a)

for i in range(1,500):
    lst.append(str(i))
lst[0]='str()'
lst[1]='str(1)'
lst[2]='str(2)'
lst[3]='str(3)'
lst[4]='str(4)'
lst[5]='str(5)'
lst[6]='str(6)'
lst[7]='str(7)'
lst[8]='str(8)'
lst[9]='str(9)'
lst[10]='str(10)'
lst[11]='str(11)'
lst[12]='str(12)'
lst[13]='str(13)'
lst[14]='str(14)'
lst[15]='str(15)'
lst[16]='str(16)'
lst[17]='str(17)'
lst[18]='str(18)'
lst[19]='
