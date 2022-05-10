import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(1)
    _pack_ = True

class TestCtypes(unittest.TestCase):

    def testSharedLibrary(self):
        raw = unittest.get_data_path('shared_library_data.raw')
        file = RawFile(raw, 's2s')
        block = file.read()[0]
        self.assertEqual(len(block.segments), 1)
        self.assertEqual(block.n_samples, 10)
        r = block.segments[0].analogsignals[0]
        self.assertEqual(len(r), 10)
        self.assert_(isinstance(r.units, ms))

        s = S()
        self.assertEqual(s.x, 1)
        s.x = 2
        r = ctypes.addressof(s.x)
        p = ctypes.c_longlong.from_address(r)
        self.assertEqual(p.value, 2)
        q = ctypes.pointer(p)

