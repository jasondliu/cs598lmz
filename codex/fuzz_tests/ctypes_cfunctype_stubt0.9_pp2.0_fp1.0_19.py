import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return range(4)

class Test_fun(TestCase):

    def test_gen(self):
        i = fun()
        self.assertIsInstance(i, range)

    def test_print(self):
        with captured_stdout() as s:
            print(fun())
        self.assertEqual(s.getvalue(), "range(0, 4)\n")

    def test_len(self):
        self.assertEqual(len(fun()), 4)

    def test_iterate(self):
        self.assertListEqual(list(fun()), [0, 1, 2, 3])

    def test_index(self):
        i = fun()
        self.assertEqual(i[1], 1)


if __name__ == "__main__":
    unittest.main()
