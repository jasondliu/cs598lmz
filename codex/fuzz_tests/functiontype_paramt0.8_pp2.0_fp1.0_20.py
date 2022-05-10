from types import FunctionType
list(FunctionType(lambda: [], {})())
</code>
This works, but is less-than-ideal for a few reasons.

<code>FunctionType</code> is non-public, but there are no obvious public alternatives.
The returned function is not anonymous.
I can't think of a way to make it return a non-callable function.

Basically, I'm looking for the <code>function()</code> constructor again, but which doesn't actually compile Python code.


A:

Well, it turns out that the <code>types</code> module does, in fact, define a public constructor for functions:
<code>from types import FunctionType as _func
def FunctionType(code, globals, name=None, argdefs=None, closure=None):
    return _func(code, globals, name, argdefs, closure)
</code>
This is more usable than the version that uses <code>FunctionType</code> directly.
One problem I had with this implementation is that their <code>code</code> object had to have an associated file name to be valid. This turned out to be a
