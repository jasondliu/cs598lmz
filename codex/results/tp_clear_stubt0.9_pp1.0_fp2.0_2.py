import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()
'''
    )

    # check that utility functions aren't taking references forever
    # (leading to unbounded RAM use) in this common case
    def test_getflags_no_reference_leak(self):
        for i in range(1_000):
            dis.get_instructions(self.bytecode)


class AttrPreTest(DisTests):

    def _disassemble(self, optimize=None):
        co = compile('42', '<string>', 'exec', optimize=optimize)
        code = co.co_code
        self.assertIsInstance(code, bytes)
        return self.disassemble(co)

    def test_optimize(self):
        have_attr_pre = getattr(self, 'attr_order', None) == 'pre'
        if have_attr_pre:
            self.assertEqual(self._disassemble(), self._disassemble(1))
            self.assertEqual(self._disassemble(), self._disassemble(2))
        else:
            with
