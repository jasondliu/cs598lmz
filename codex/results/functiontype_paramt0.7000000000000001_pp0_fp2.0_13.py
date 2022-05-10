from types import FunctionType
list(FunctionType(1, 2, 3, 4, 5))

print('\n')
print('callable(): ')
print('\n')

print(callable(1))
print(callable(int))
print(callable(callable(int)))
print(callable('callable'))

print('\n')
print('reversed(): ')
print('\n')

print(list(reversed(range(1, 10))))

print('\n')
print('round(): ')
print('\n')

print(round(1.5))
print(round(1.51, 1))
print(round(1.5, 1))
print(round(1.6, 1))
print(round(1.5, 2))
print(round(1.5, 3))
print(round(1.5, 4))

print('\n')
print('sum(): ')
print('\n')

print(sum((1, 2, 3)))
print(sum((1, 2, 3), -6))
print(sum((1
