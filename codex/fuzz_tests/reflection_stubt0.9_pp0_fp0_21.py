fn = lambda: None
gi = (i for i in ())
fn.__code__ = CompiledCode(
    argcount=0, nlocals=0, stacksize=2, flags=67,
    code='d\x00Z',
    consts=(None,),
    names=(),
    varnames=(),
    filename='<stdin>',
    name='<module>',
    firstlineno=1,
    lnotab='\x00\x01',
    freevars=(),
    cellvars=(),
)

fn2 = lambda: None
fn2.__code__ = CompiledCode(
    argcount=0, nlocals=0, stacksize=2, flags=67,
    code='d\x00S\x00',
    consts=('test',),
    names=(),
    varnames=(),
    filename='<stdin>',
    name='<module>',
    firstlineno=1,
    lnotab='\x00\x01',
    freevars=(),
    cellvars=(),
)
print(fn2.__code__.co_code[:-1])
