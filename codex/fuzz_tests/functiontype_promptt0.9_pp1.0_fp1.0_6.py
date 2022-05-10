import types
# Test types.FunctionType in builtin_isinstance(), assuming the cpyext API
# doesn't allow testing arbitrary extension types.
def f():
    pass
assert builtin_isinstance(None, (type(None), int))
assert builtin_isinstance(0, (type(None), int))
assert builtin_isinstance(f, (types.FunctionType,))
assert not builtin_isinstance(f, (types.BuiltinFunctionType,))
assert not builtin_isinstance(f, (types.BuiltinFunctionType(),))
assert not builtin_isinstance(f, 'anything')


import py

# Tests for py.path.local
class AppTestPyPathLocal:

    def setup_method(self, method):
        import os
        self.file = __file__
        self.dir = os.path.dirname(__file__)
        self.basename = os.path.basename(self.file)
        self.purebasename, self.ext = os.path.splitext(self.basename)

    def test_local_dir(self):
        import
