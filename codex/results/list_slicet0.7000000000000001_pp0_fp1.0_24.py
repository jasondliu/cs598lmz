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
</code>
Это обычный хак. Он просто ждет пока появится объект в памяти и потом его удаляет. Я так понимаю в исходном коде не будет такого хака?
Если же нет то давайте немного подробнее разберёмся
Это конечно не странно что в памяти появился
