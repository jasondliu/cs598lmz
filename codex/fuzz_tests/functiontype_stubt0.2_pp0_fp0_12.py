from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) is FunctionType)
print(type(a) is GeneratorType)
print(type(a) is type)
print(type(a) is type(type))
print(type(a) is type(type(type)))
print(type(a) is type(type(type(type))))
print(type(a) is type(type(type(type(type)))))
print(type(a) is type(type(type(type(type(type))))))
print(type(a) is type(type(type(type(type(type(type)))))))
print(type(a) is type(type(type(type(type(type(type(type))))))))
print(type(a) is type(type(type(type(type(type(type(type(type)))))))))
print(type(a) is type(type(type(type(
