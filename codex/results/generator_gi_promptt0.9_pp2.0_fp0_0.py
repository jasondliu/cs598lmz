gi = (i for i in ())
# Test gi.gi_code attribute with code object
print(gi.gi_code)
# AttributeError: 'generator' object has no attribute 'gi_code'


# Creating generator with stopping at given index
def gensquares(N):
    for i in range(N):
        yield i**2

for i in gensquares(10):
    print(i)

for i in gensquares(5):
    print(i)
print('#' * 52 + '  A genexpr is just sugar on top of a generator comprehension')

# Genexp is syntactic sugar on top of generator comprehension
G = (i**2 for i in range(4))

# Equal to this construction but with Genexp
G = (i**2 for i in range(4))
for i in G:
    print(i)
print('#' * 52 + '  A genexp is also syntactic sugar on top of a generator functions with a yield statement')
print('#' * 52 + '  When we run a genexp, what Python actually does is create a generator object.')
print('#' * 52 +
