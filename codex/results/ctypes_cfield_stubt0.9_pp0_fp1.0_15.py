import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class TestConstant:
    def test_simple(self):
        assert 42 == 42
        assert type(42) is int

    def test_dtypes(self):
        b = 4 + 3.2j
        assert type(b) is complex
        assert complex is type(b)
        assert complex is complex
        assert type(1) is int

    def test_module_builtin(self):
        import builtins
        assert builtins.float is float

    def test_builtin_global(self):
        assert True is True

    def test_subsubsubmodule(self):
        import os
        import os.path
        import os.path.os2emxpath
        import os.path.os2emxpath.stuff

        assert os.path.os2emxpath.stuff is os.path.os2emxpath.stuff


class TestBuiltinName:
    def test_functionality(self):
        import builtins
        f = builtins.len
        assert f is builtins.len
        assert f is len
        assert len is f

