from types import FunctionType
a = (x for x in [1])

print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, type(iter([]))))
print(isinstance(a, type(iter(()))))

print(type(iter([])))
print(type(iter(())))

print(type(iter(a)))
print(isinstance(iter(a), GeneratorType))

print(type(iter(iter(a))))
print(isinstance(iter(iter(a)), GeneratorType))

print(type(iter(iter(iter(a)))))
print(isinstance(iter(iter(iter(a))), GeneratorType))

print(type(iter(iter(iter(iter(a))))))
print(isinstance(iter(iter(iter(iter(a)))), GeneratorType))

print(type(iter(iter(iter(iter(iter(a)))))))
print(isinstance(iter(iter(iter(iter(iter(a))))), GeneratorType))

print(type(iter(iter(iter(iter(iter(iter
