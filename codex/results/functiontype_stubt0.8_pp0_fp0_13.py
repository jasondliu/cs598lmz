from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = 'abc'
d = {'a': 1}
e = FunctionType('foo', globals(), {'a': 1})
f = zip([1, 2, 3], [4, 5, 6])
g = range(1, 10)

print(a.__iter__)
print(b.__iter__)
print(c.__iter__)
print(d.__iter__)
print(e.__iter__)
print(f.__iter__)
print(g.__iter__)

#<method-wrapper '__iter__' of generator object at 0x1015c12b0>
#<method-wrapper '__iter__' of list object at 0x1015c1288>
#<method-wrapper '__iter__' of str object at 0x1015c12a0>
#<method-wrapper '__iter__' of dict object at 0x1015c1248>
#<bound method FunctionType.__iter__ of <function foo at 0x1015d2a60>>
#
