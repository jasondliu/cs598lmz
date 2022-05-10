from types import FunctionType
list(FunctionType(f.__code__, {}, name='f', argdefs=(), closure=([c.cell_contents])))
</code>

