from types import FunctionType
list(FunctionType(*f.__reduce__()) for f in map) # or filter, etc
</code>
But that seems pretty hacky to me, and it fails to handle stateful <code>map</code> and <code>filter</code> functions.
Is there a more idiomatic way to do this?


A:

I found the <code>copyreg</code> module.
<code>import copyreg

def map_reduce(obj):
    return map, (obj.func, obj.it)
copyreg.pickle(map, map_reduce)

def filter_reduce(obj):
    return filter, (obj.func, obj.it)
copyreg.pickle(filter, filter_reduce)

import pickle

l = [1, 2, 3, 4, 5]
with open('test.pickle', 'wb') as f:
    pickle.dump([map(lambda x: x * 2, l), filter(lambda x: x &lt; 4, l)], f)

with open('test.pickle', 'rb') as f:

