import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.ccc=a
tt=a
while tt:tt.c=a;tt=tt.c
keepalive.append(a)
weakref.finalize(a,lst,callback)
del a
"""
        n = 100
        for i in range(200):
            #print "*",i
            res = self.interpret(s, [])

    def test_finalizer_lst_3(self):
        def callback(x):
            i = 99
        class A(object):
            pass
        a = A()
        a.x = A()
        a.x.x = a
        lst = ["a"]
        weakref.finalize(a.x, lst, callback)
        del a.x.x
        del a.x

    def test_finalizer_lst_2(self):
        class A(object):
            def __init__(self, lst):
                self.lst = lst
            def f(self):
                self.lst.append(1)
        lst = []
