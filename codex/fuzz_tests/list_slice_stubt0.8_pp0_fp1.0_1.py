import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
del a
del keepalive
lst=None
del lst
A()
lst=[]
del lst
gc.collect()
class C:
    def f0(self):self.f1()
    def f1(self):self.f2()
    def f2(self):self.f3()
    def f3(self):self.f4()
    def f4(self):self.f5()
    def f5(self):self.f6()
    def f6(self):self.f7()
    def f7(self):self.f8()
    def f8(self):self.f9()
    def f9(self):self.f10()
    def f10(self):self.f11()
    def f11(self):self.f12()
    def f12(self):self.f13()
    def f13(self):self.f14()
    def f14(self):self.f15()
    def f15(self):self.f16()
    def
