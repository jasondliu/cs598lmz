import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
del lst[0]
del keepali0e
del a
del lst
print('Pass')
import weakref
import gc
class A(object):pass
a=A()
a.c=a
ref=weakref.ref(a,lambda x:None)
del a
if ref()is None:print('Pass')
import decimal
class A(object):__slots__=('value',)
class B(A):__slots__=('name',)
a=A()
a.value=42
b=B()
b.value=42
b.name='spam'
print(decimal.Decimal('1.3').as_integer_ratio())
print(decimal.Decimal('-Infinity').as_integer_ratio())
print(decimal.Decimal('NaN').as_integer_ratio())
print(decimal.Decimal('sNaN').as_integer_ratio())
print(decimal.Decimal('sNaN123').as_integer_ratio())
