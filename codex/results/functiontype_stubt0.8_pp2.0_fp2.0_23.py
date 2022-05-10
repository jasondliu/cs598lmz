from types import FunctionType
a = (x for x in [1])
# time.sleep(0.1)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(dir(a))
