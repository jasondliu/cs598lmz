import bz2
bz2.compress().decompress()

>>> import lzma
lzma.compress().decompress()


Introspection
=============

>>> import timeit
>>> timeit.timeit(stmt="import fibonacci", number=100, setup="pass")
16.87604879771684
>>> timeit.timeit(stmt="fibonacci.fib(1000)", number=1000, setup="import fibonacci")
0.4119829201209278

>>> timeit.repeat(stmt="import fibonacci", number=10, repeat=10, setup="pass")
[14.510374265943561, 16.848506657972066, 16.531554553412418, 16.980488827749024, 17.328463893564677, 15.989833128927854, 14.368804914887072, 14.13789318999949, 14.908596726865589, 14.814918701579135]

>>> timeit.repeat(stmt="fib
