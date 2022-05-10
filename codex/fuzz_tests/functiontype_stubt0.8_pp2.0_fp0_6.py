from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType) #True

>>> def f():
	print("Hi!")
isinstance(f, FunctionType) #True

from types import MethodType
f.name = "Hi!"
isinstance(f, MethodType) #True

>>> a = 3, 4
type(a) == tuple #True

>>> a = [1, 2, 3]
type(a) == list #True

from types import MappingProxyType
a = {"a": 1}
a_proxy = MappingProxyType(a)
a_proxy #mappingproxy({'a': 1})

>>> class MyClass:
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return f"MyClass(value={self.value})"
	def __repr__(self):
		return f"MyClass(value={self.value})"
a = MyClass(42)
b = MyClass(42)
a is b #False

>>> class MyClass:
	def __init__(
