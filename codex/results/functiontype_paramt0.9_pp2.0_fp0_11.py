from types import FunctionType
list(FunctionType())
#!TypeError: descriptor '__iter__' of 'list' object needs an argument
 
# In python 3
list(iter(FunctionType, 1))
# []
 
# In python 2, integers are iterable:
list(1)
# [0]
 
# In python 2, strings are iterable:
list("hello")
# ['h', 'e', 'l', 'l', 'o']
 
# In python 3, strings are not iterable and hence an exception will be raised:
list("hello")
#!TypeError: 'str' object is not iterable
 
# In python 2, you can say:
sum(n for n, p in zip(numbers,primes) if p)
# 6
 
# In python 3, you have to say:
sum(n for n, p in zip(numbers,primes) if p)
# 6
 
# In python 2, a generator expression will produce a list:
(n for n, p in zip(numbers,primes) if p)
# [2, 3]
 
#
