import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(i32)
    _fields_ = [x]

class Test(BaseTestCase):
    def test(self):
        self.assertEqual(S.x.item.name, 'x')

if __name__ == "__main__":
    unittest.main()
