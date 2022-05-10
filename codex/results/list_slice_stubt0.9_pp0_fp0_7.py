import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=callback
keepali0e.append(a)
del a
"""
GA = """; __pypy__.recursive_repr.set_limit(2); __pypy__.recursive_repr.set_limit(1000)
dic={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
class A(object):
    def f(self, a):return a
class B(A):
    def f(self,a):return "B"+a+"B"
class C(A):
    def f(self,a):return "C"+a+"C"
class D(A):
    def f(self,a):return "D"+a+"D"
class E(A):
    def f(self,a):return "E"+a+"E"
class F(A):
    def f(self,a):return "F"+a+"F"
class G(A):
