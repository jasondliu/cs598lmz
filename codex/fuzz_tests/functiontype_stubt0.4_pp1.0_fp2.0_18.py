from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

print(type(type))
print(type(int))
print(type(type(1)))

print(type(object))
print(type(object()))

print(type(type))
print(type(type(type)))

print(type(super))
print(type(super(int)))
print(type(super(int, 1)))

# print(type(dict))
# print(type(dict()))
# print(type(dict.fromkeys))

print(type(list))
print(type(list()))
print(type(list.append))

print(type(set))
print(type(set()))
print(type(set.add))

print(type(tuple))
print(type(tuple()))
print(type(tuple.count))

print(type(str))
print(type(str()))
print(type(str.capitalize))

print(type(bytes))
print(type
