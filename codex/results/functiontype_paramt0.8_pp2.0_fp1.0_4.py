from types import FunctionType
list(FunctionType(lambda v: v, list(range(5))))

a = list(map(lambda v: v**2, list(range(5))))


# Task #1
print("\n=== Task #1 ===")

a = list(range(100))

b = list(filter(lambda v: v % 3 == 0, a))
print(b)

b = list(map(lambda v: v**2 if v % 3 == 0 else v, a))
print(b)


# Task #2
print("\n=== Task #2 ===")

squared = lambda v: v**2
print(squared)
quit(squared(2))

def squared(v):
	return v**2
print(squared)
quit(squared(2))


# Task #3
print("\n=== Task #3 ===")

def squared(v):
	return v**2

print(squared(2))
print(squared.__doc__)
print(squared.__name__)


# Task #4
print("\n=== Task #
