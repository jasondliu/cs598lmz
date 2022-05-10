import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

'''

import weakref

class C(object):
    callback_func = 0
    def __init__(self):
        print "__init__"
        self.b = [func for func in dir(self) if callable(getattr(self, func)) if func.startswith("my")]
        self.b = weakref.WeakValueDictionary()
        self.b["1"] = self.my_test()
        self.b["2"] = self.my_func()

    @classmethod
    def callback(cls, x):
        print "A.__del__"

    def my_test(self):
        print "my_test"
        return 1

    def my_func(self):
        print "my_func"
        return 2

    def __del__(self):
        print "__del__"
        #del self.b["1"]


C.callback_func = C.callback
a = C()

a.b["1"]()
#a.b["
