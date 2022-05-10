from types import FunctionType
list(FunctionType(lambda x: 2 * x, {}, 'f', (2 * 2 * x for x in range(3)),
    3).gi_code.co_consts)[1] is (2 * 2 * x for x in range(3))
True
</code>
You could also look for iterators and generators by examining the closure cells, which is performed by the following function:
<code>def gen_iter_cells(f):
    if not isinstance(f, FunctionType):
        raise TypeError("cell_gen_iter_cells() only supports functions")
    for i, c in enumerate(f.__closure__):
        obj = c.cell_contents
        if isinstance(obj, GeneratorType):
            yield "&lt;generator #%d at 0x%x, code=%s&gt;" % (i, id(c),
                    repr(obj.gi_code))
        elif isinstance(obj, IteratorType):
            yield "&lt;iterator #%d at 0x%x&gt;" % (i, id(c))
</code>
You may want
