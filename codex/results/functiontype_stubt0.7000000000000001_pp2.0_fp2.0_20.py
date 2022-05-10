from types import FunctionType
a = (x for x in [1])
a.next()

# another key thing is that it is an iterator
# like any iterator, it can be used in for loops

# this is an iterator of all the numbers from 1 to 10
a = (x for x in range(1, 11))
for x in a:
    print(x)

# If you want to convert it into a python list
# you can use the list function

a = (x for x in range(1, 11))
a = list(a)
print(a)

# you can also use a generator to make a list
# this example shows how to make a list of all
# the square numbers from 1 to 10

def squares(n):
    for i in range(1, n+1):
        yield i**2

a = list(squares(10))
print(a)

# this example shows how to use a generator to
# make a list of all the primes from 2 to 20

def primes(n):
    for i in range(2, n+1):
        for j in range(2, i):
           
