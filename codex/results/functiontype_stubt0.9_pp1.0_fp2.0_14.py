from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(enumerate))
print(type(lambda x:x+1))
print(type((x for x in [1])))
print(type(abs))
print(type(sys))

def factorial(x):
  if x < 1:
    return 1
  return x * factorial(x - 1)

print(factorial(5))
fact = factorial
print(fact(5))
print(map(fact, range(6)))
print(list(map(fact, range(6))))

def inverse(x):
  return 1.0 / x

print(list(map(inverse, range(1, 11))))
print([inverse(i) for i in range(1, 11)])
print(list(map(str, range(1, 11))))

print(list(filter(lambda x: x % 2 == 1, range(1, 20))))


def is_odd(x):
  return x % 2 == 1

print(list(filter(is_odd, range(1, 20))))

