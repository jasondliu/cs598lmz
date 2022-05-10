import ctypes
# Test ctypes.CFUNCTYPE
_Prototype = ctypes.CFUNCTYPE(ctypes.c_char_p)
class TestCFUNCTYPE:
    def test_instance(self):
        self.assertRaises(TypeError, _Prototype, 1)
        self.assertRaises(TypeError, _Prototype, "")
        self.assertRaises(TypeError, _Prototype, None)
        self.assertRaises(TypeError, _Prototype, [])
        self.assertRaises(TypeError, _Prototype, {})
        self.assertRaises(TypeError, _Prototype, ())

    def test_call(self):
        p = _Prototype(lambda : "Hello")
        self.assertEqual(p(), "Hello")
        self.assertEqual(p(), "Hello")
        self.assertEqual(p(), "Hello")

        def func():
            return "He" + "llo"

        p = _Prototype(func)
        self.assertEqual(p(), "Hello")
        self.assertEqual(p(), "Hello")

