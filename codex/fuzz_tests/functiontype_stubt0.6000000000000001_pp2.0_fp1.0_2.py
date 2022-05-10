from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))

print(isinstance(a, GeneratorType))
print(isinstance(lambda x: x, GeneratorType))

print(callable(a))
print(callable(lambda x: x))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(a, FunctionType))

print('\n')


class A(object):
    def __call__(self):
        print('__call__')

a = A()
a()
print(callable(a))
print(isinstance(a, FunctionType))

print('\n')


class A(object):
    def __call__(self, *args, **kwargs):
        print('__call__')

    def __len__(self):
        print('__len__')
        return 1


a = A()
print(len(a))
a()
print(callable(a))
print(isinstance(a, FunctionType))
print('\n')


class A(object):
