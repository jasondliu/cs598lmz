gi = (i for i in ())
# Test gi.gi_code is <code object <genexpr> at 0x..., file ..., line 1>
# Note no docstring and no co_consts
def f():
    global gi
    yield from gi
def g():
    global gi
    yield from (i for i in ())

# Test rangeiterator is <rangeiterator object at 0x...>
# Note no docstring and no co_consts
def f():
    global rgi
    yield from rgi
def g():
    global rgi
    yield from range(0)

# Test mapiterator is <mapobject iterator>
# Note no docstring and no co_consts
def f():
    global mapi
    yield from mapi
def g():
    global mapi
    yield from map(lambda x: x, [])

# Test chainiterator is <itertools.chain object at 0x...>
# Note no docstring and no co_consts
def f():
    global chaini
    yield from chaini
def g():
    global chaini
    yield from itertools.chain([])

#
