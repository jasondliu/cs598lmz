from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals)
print(b(10))
</code>
But can't figure out how to create a <code>GeneratorType</code> from the same information. Any ideas?


A:

The generator you're creating is a generator function, as opposed to a generator expression.  A generator function is a function that returns a generator.  To get the generator from that function, you need to call it.
<code>b(10)
</code>
Will return the result you're expecting.  The following is equivalent to the code you posted:
<code>def a(x):
    yield x

b = a

c = b(10)

print(c.__next__()) # or next(c)
</code>

