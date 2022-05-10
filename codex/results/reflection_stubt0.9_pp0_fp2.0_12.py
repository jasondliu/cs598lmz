fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_firstlineno

def test_fc_code():
    opcode = _testcapimod.opcode
    space = gettestobjspace(**{"objspace.opcodes.CALL_FUNCTION": opcode})
    def f(): pass
    code = Code(space, space.getexecutioncontext())
    code.co_firstlineno = 0
    code.co_freevars = ['abc', 'def']
    code.co_nlocals = 2
    assert type(code) is PyCode
    assert code.co_firstlineno == 0
    assert code.co_freevars == ['abc', 'def']
    assert code.co_nlocals == 2
    assert type(code.co_code) is str
    assert len(code.co_code) == 0
    assert type(code.co_filename) is str
    assert type(code.co_name) is str
    assert type(code.co_lnotab) is str
    assert type(code.co_names)
