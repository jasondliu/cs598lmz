gi = (i for i in ())
# Test gi.gi_code is not NULL and gi.gi_frame is NULL
try:
    gi.gi_code
except ValueError:
    raise unittest.SkipTest("test is only applicable to Cython-generated generators")

if gi.gi_frame is not None:
    raise unittest.SkipTest("test is only applicable to CPython")


class TestCAPI_PyGen_New(CAPIpgenTests):
    '''Test PyGen_New()'''

    def test_PyGen_New(self):
        code = compile('i for i in ()', '', 'exec')
        gi = PyGen_New(code)
        # Test gi.gi_code is not NULL and
        # gi.gi_frame is NULL,
        # Check gi_code is the same object as received by PyGen_New
        self.assertEqual(gi.gi_code, code)
        self.assertIs(gi.gi_frame, None)
        # Check gi_running is 0
        self.assertEqual(gi.gi_running, 0)

