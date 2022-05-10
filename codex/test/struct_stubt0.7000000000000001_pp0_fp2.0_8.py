from _struct import Struct
s = Struct.__new__(Struct)
s.format='I 2s f'
print(s.size)

import sys
print(sys.stdout.write('hello world\n'))

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n*factorial(n-1)
print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact = factorial
print(fact)
print(fact(5))

map(factorial, range(11))
print(list(map(factorial, range(11))))

list(map(fact, range(11)))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True))

def reverse(word):
    return word[::-1]

print(reverse('testing'))

print(sorted(fruits, key=reverse))

