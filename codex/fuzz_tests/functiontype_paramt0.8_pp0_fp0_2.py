from types import FunctionType
list(FunctionType(x, y, z) for x in ..... for y in .... for z in .....)
</code>
The point is, if you have an iterable of the same objects over which you iterate, it's kind of natural to use the nested <code>for</code> loops.

