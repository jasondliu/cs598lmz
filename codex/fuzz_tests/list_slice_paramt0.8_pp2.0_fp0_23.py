import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
if lst:print("hey")
lst[0]+=str()
print("end")
"""
#@-node:<< Example >>
#@nl
#@-node:Tests
#@+node:WeakValueDictionary
class WeakValueDictionary(dict):
    """
    A dictionary whose values are weak references.
    Functions like a normal dictionary except that when object
    is no longer referenced elsewhere, it is removed from the
    dictionary.
    """
    def __init__(self,initDict=None):
        if initDict:
            for key,value in initDict.items():
                self[key]=value
    def __getitem__(self,key):
        """
        Returns the value associated with the key.
        """
        return self.data[key()]
    def __setitem__(self,key,value):
        """
        Store a new value under the given key.  If the key is a
        weak reference to an object that no longer exists,
        then nothing is changed.
        """

