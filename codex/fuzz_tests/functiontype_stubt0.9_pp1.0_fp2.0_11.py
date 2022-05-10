from types import FunctionType
a = (x for x in [1])
print(isinstance(a, type(lambda: None)))

a = 1
a_i = iter(a)
print(a_i is iter(a_i))
print(iter(None) is iter(None))

module_name = __name__
module_name = '__main__'

a = (1, )

print(type(True.__class__))
print(type(True).__bases__)
print(type('a').__bases__)

type_dic = type.__dict__
type_type = type.__class__
print(type_dic)
print(type_dic is type_type.__dict__)

print(type(type(int)))
print(type(int))
print(type(type(int)))
print(type(type).__bases__)
print(type(type(int)).__bases__)
print(type(object).__bases__)
print(type(object.__class__).__bases__)
print(type(type(int)))
print(type
