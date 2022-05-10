import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
#['']
</code>
Не могу понять, почему не происходит вызов функции callback после удаления объекта a. Ведь там есть циклическая ссылка. Как надо изменить код, чтобы произошёл вызов функции callback?


A:

Потому что после удаления переменной <code>a</
