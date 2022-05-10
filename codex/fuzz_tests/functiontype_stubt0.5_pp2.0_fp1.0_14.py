from types import FunctionType
a = (x for x in [1])
a

def test():
    print('test')

test()

print(type(test))
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(test, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(test, GeneratorType))

'''
def test():
    print('test')

a = test()
print(a)
'''
