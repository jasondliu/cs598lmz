gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_GENERATOR)
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti

# Test PyCell_Get
x = y = 10
def f():
    x = 1
    y = 2
    def g():
        def h():
            return x + y
        return h
    return g()
print(f()())

# Test dict_itemsiterator
it = iter({1: 2, 3: 4}.items())
print(list(it))

# Test dict_keysiterator
it = iter({1: 2, 3: 4})
print(list(it))

# Test dict_valuesiterator
it = iter({1: 2, 3: 4}.values())
print(list(it))

# Test listiterator and rangeiterator
it = iter(range(2))
print(list(it))
it = iter([1, 2, 3])
print(list(it))

# Test tupleiterator
it = iter((1, 2, 3))
