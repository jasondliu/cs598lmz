from _struct import Struct
s = Struct.__new__(Struct)
s.size = 25
s.format = 'iiiif'
print s
s = Struct.__new__(Struct)
s.size = 25
s.format = 'iiiif'
print s
"""
,   ###
""".__getitem__((0,))
)
        t, c, o = self.check(code)
        assert not o.run
        assert c['{}.__getitem__'.format(t.name)]
        assert c['{}.__init__'.format(t.name)]

    @py.test.mark.skipif('not has_cffi')
    def test_struct2(self):
        code = py.code.Source("""
from _struct import Struct
s = Struct('iiiif')
"""
)
        t, c, o = self.check(code)
        assert not o.run
        assert c['{}.__init__'.format(t.name)]
        assert c['{}.__getitem__'.format(t.name)]
        assert c['{}.__new__'.format(t.name)]

   
