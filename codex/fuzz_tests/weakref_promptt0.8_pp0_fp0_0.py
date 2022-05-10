import weakref
# Test weakref.ref:

f = open('temp.txt','w' )
f.write('python')

f_ref = weakref.ref(f)

f_ref()
f_ref().read()
f.close()
f_ref() is None
f_ref().read()
f_ref() is None
f_ref().close()
f_ref() is None
 
# Test weakref.WeakValueDictionary

import weakref
import gc

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()

d['primary'] = a
d['primary']

gc.collect()
d
class MyList(list):
    pass

l1 = MyList()
l2 = MyList()

l1.append(l2)
l2.append(l1)

l1
l2
import weakref

a = [1, 2, 3]
b = [a, 4]
a.append(b)

wd = weakref.WeakValueDictionary()
wd["primary"] = a

