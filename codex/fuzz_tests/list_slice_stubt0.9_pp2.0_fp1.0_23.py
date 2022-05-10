import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
t=weakref.ref(a,callback)
keepalive.append(t)
del a
while len(lst):
    time.sleep(0.01)
    lst.append(str())
</code>
Приведенный пример делает следующее: 

Создаем объект типа <code>A</code> и дочерний объект от типа <code>A</code> (именно дочерний, не наследованный), называем его <code>a</code> и добавляем ссылку на него.
