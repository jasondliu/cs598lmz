from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('*'*40)

b = (x for x in range(10))
print(type(b))  # <class 'generator'>
print(type(b) == types.GeneratorType)  # True
print(isinstance(b, types.GeneratorType))  # True

print('*'*40)

c = [x for x in range(10)]
print(type(c))  # <class 'list'>
print(type(c) == types.GeneratorType)  # False
print(isinstance(c, types.GeneratorType))  # False


def check_generator(obj):
    if isinstance(obj, types.GeneratorType):
        print('Yes, this object is a generator')
    else:
        print('No, this object is not a generator')


check_generator([x for x in range(10)])  # No, this object is not a generator
check_generator((x for x in range(10
