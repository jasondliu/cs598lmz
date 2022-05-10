import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
del a
del lst
del callback
import gc
gc.collect()

# 使用weakref.ref创建弱引用
import weakref
a_set={"one",2,"three"}
wref=weakref.ref(a_set)
print(wref)
print(wref())
a_set={'one',2}
print(wref())
print(wref() is None)

# 使用weakref.WeakValueDictionary创建弱引用
import weakref
class Cheese(object):pass
stock=weakref.WeakValueDictionary()
catalog=[Cheese(),Cheese(),Cheese()]
for cheese in catalog:
    stock[cheese.__repr__()]=cheese
print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys
