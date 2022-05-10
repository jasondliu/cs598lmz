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
    del lst
#创建用于监视弱引用的类，该类可通过非循环引用的对象跟踪到循环引用的对象，并在循环引用的对象被回收后调用回调函数
class WeakCallbackReferences(object):
    def __init__(self,callback):
        self._callback=callback
        self._objects={}
        def __getitem__(self,object):
            oid=id(object)
            ref=self._objects.get(oid)
            if ref is None:
                ref=weakref.ref(object,self._removeObject)
                self._objects[oid]=ref
            return ref
        def _removeObject(self,ref):
            oid=id(ref)

