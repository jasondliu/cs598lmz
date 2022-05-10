from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))  # True
print(isinstance(a, Iterable))  # True
print(isinstance(a, Generator))  # True
print(isinstance(a, FunctionType))  #False

print(isinstance(range(10), Iterator))  # False
print(isinstance(range(10), Iterable))  # True
print(isinstance(range(10), Generator))  # False
print(isinstance(range(10), FunctionType))  #False

for i in a:
    print(i)
print('--'*10)
for i in range(10):
    print(i)

print('--' * 20)
b = iter([1,2,3])
c = iter(a)

print(isinstance(b, Iterator))  # True
print(isinstance(b, Iterable))  # True
print(isinstance(b, Generator))  # False
print(isinstance(b, FunctionType))  # False

print(isinstance(c, Iterator))  # True
print(
