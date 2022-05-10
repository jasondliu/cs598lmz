import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a,callback))
del a
while lst:print len(lst),lst
#Выведет
#2 ['']
#1 ['']
#0 []
#А вот если все переменные  удалить и в конце-
#del callback,lst,keepali0e
#То получим
#2 ['']
#2 ['']
#2 ['']
#2 ['']
#А если удалить не все переменные то получим
#2 ['']
#1 ['']
#0 []
#Т.е. элменты списка уда
