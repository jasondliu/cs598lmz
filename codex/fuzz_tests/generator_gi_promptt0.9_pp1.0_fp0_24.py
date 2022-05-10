gi = (i for i in ())
# Test gi.gi_code.co_zombi is not defined for __iter__ method
print(gi.gi_code.co_zombi)
</code>
Output:
<code>&lt;stdin&gt;:4: DeprecationWarning: co_zombi was an internal flag, does not map to Python 3
    print(gi.gi_code.co_zombi)
</code>
Question: How can I identify a generator object using an attribute or method of <code>code</code> object?


A:

According to docs, the CPython interpreter adds attributes, starting with double <code>co_</code> prefix, to the code objects <code>CO_OPTIMIZED</code> flag.
How to get this flag:
<code>def is_generator(func):
    return getattr(func.__code__, 'co_flags', object()) &amp; CO_GENERATOR or False
</code>
The code object of a generator function has this flag <code>CO_GENERATOR</code> set.

