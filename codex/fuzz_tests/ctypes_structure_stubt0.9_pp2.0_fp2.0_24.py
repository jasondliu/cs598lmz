import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_uint
    z = ctypes.c_ubyte

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(DOCTest('test_zero_fill'))
    suite.addTest(DOCTest('test_one_fill'))
    suite.addTest(DOCTest('test_one_class'))
    suite.addTest(DOCTest('test_one_Structure'))
    suite.addTest(suite_from_doctest(ctypes.c_bool))
    suite.addTest(suite_from_doctest(ctypes.c_char))
    suite.addTest(suite_from_doctest(ctypes.c_byte))
    suite.addTest(suite_from_doctest(ctypes.c_ubyte))
    suite.addTest(suite_from_doctest(ctypes.c_short))
    suite.addTest(suite_from_doctest
