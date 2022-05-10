from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(map))
print(type(FunctionType))
print(type(FunctionType))
print(type(FunctionType()) == FunctionType)
print(type(FunctionType) == FunctionType)

print(type(FunctionType) == type)
print(type(FunctionType) == type(FunctionType))
print(type(FunctionType) == type(type))

print(type(type))
print(type(type(type)))

print(type(type) == type)
print(type(type) == type(type))
print(type(type) == type(type(type)))

print(type(type(type)) == type)
print(type(type(type)) == type(type))
print(type(type(type)) == type(type(type)))

print(type(type(type)))
print(type(type(type(type))))
print(type(type(type(type(type)))))

print(type(type(type(type(type)))) == type)
print(type(type(type(type(type))))
