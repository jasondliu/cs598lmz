from types import FunctionType
a = (x for x in [1])
print(isinstance(a, (GeneratorType, FunctionType)))

result = [x * x for x in range(10) if x % 2 == 0]
print(result)
print(isinstance(result, (GeneratorType, FunctionType)))

result = (x * x for x in range(10) if x % 2 == 0)
print(result)
print(isinstance(result, (GeneratorType, FunctionType)))

print(a.gi_frame)
print(a.gi_running)
print(a.gi_code)
print(a.gi_yieldfrom)

import inspect
for name, value in inspect.getmembers(a):
    if name.startswith('__'):
        continue
    print(name, ":", value)

import dis
print(a.__code__.co_code)
print(dis.Bytecode(a.__code__))
