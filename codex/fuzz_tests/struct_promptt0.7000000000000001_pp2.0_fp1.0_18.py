import _struct
# Test _struct.Struct

def test_struct_int_args(space):
    s = space.appexec([], """():
        import _struct
        return _struct.Struct('i')""")
    w_res = space.appexec([s], """(s):
        return s.size, s.format""")
    assert space.unwrap(w_res) == (4, 'i')

def test_struct_char_args(space):
    s = space.appexec([], """():
        import _struct
        return _struct.Struct('ci')""")
    w_res = space.appexec([s], """(s):
        return s.size, s.format""")
    assert space.unwrap(w_res) == (5, 'ci')

def test_struct_p_args(space):
    s = space.appexec([], """():
        import _struct
        return _struct.Struct('pi')""")
    w_res = space.appexec([s], """(s):
        return s.size, s.format""")
   
