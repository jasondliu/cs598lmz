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
import weakref
class A(object):pass
class B(object):pass
def callback(weak):print('callback with ',type(weak).__name__)
def onref(weak):print('onref with ',type(weak).__name__)
b=B()
while lst:del lst[0]
b=B()
one=A()
one.bc=b
two=A()
two.bc=two
three=A()
three.bc=three
refone=weakref.ref(one,callback="onref")
reftwo=weakref.ref(two,callback=onref)
refthree=weakref.ref(three,callback=onref)
print('del one,before',refone(),reftwo(),refthree())
del one
print('del one,after ',refone(),reftwo(),refthree())
print('del two,before',refone(),reftwo(),refthree())
del two
print('del two,after ',refone(),reftwo(),refthree())
del three
print('
