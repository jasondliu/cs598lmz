import gc, weakref

class C(object): pass

weak_obj_dict = weakref.WeakKeyDictionary()

for i in range(20):
    obj = C()
    weak_obj_dict[obj] = i
    del obj

for i in range(20):
    obj = C()
    obj.attr = i
    del obj

# force a garbage collection cycle.
# GC should have collected the weakref'ed
# the object, but it didn't...
gc.collect()

print('{0} objects in weak_obj_dict'.format(len(weak_obj_dict)))
</code>
Basically, I create 20 instances of class <code>C</code>, which I insert in a <code>weakref.WeakKeyDictionary</code>. Then I delete those instances, and create 20 new ones, thus assuming that the <code>WeakKeyDictionary</code> would now be empty. However, <code>gc.collect</code> gives me this output:
<code>20 objects in weak_obj_dict
</code>
How can I force <code>WeakKeyDictionary</
