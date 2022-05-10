import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

class Test(unittest.TestCase):
    def test_1(self):
        f = lambda x: 2*x
        fp = FUNTYPE(f)
        self.assertEqual(fp(1.0),2.0)
        self.assertEqual(fp(2.0),4.0)

    def test_2(self):
        f = lambda x: 2*x
        fp = FUNTYPE(f)
        self.assertEqual(fp(1.0),2.0)
        self.assertEqual(fp(2.0),4.0)


if __name__ == '__main__':
    unittest.main()
</code>

