from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__["_fmt"] = ">L"
s.__dict__["format"]

f = Foo()
f.__dict__["_fmt"] = ">L"
f.__dict__["format"]
"""
        d = {}
        exec text in d
        assert d["x"] == f.format
        assert d["y"] == s.format

    def test_struct_new_format(self):
        def raises(exc, f):
            try:
                Struct(f)
            except exc:
                pass
            else:
                assert False, "Did not raise"

        raises(TypeError, None)
        raises(TypeError, 1)
        raises(TypeError, {})
        raises(TypeError, object())
        raises(TypeError, 1+5j)

    def test_struct_set_format(self):
        def raises(exc, f):
            try:
                s = Struct()
                s.format = f
            except exc:
                pass
            else:
                assert False, "Did not raise"


