import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst))
del a
```

Now we have a list and a reference loop that deletes the list. The string in the list should also be freed and it will be if we use the count-then-sweep algorithm:

```
>>> gc.set_debug(gc.DEBUG_STATS)
>>> gc.collect()
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
gc: collectable <list 0x7f4c4b4d8908>
