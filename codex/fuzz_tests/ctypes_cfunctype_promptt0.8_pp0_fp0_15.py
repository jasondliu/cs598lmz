import ctypes
# Test ctypes.CFUNCTYPE c_double, c_double
class CtypesTest(unittest.TestCase):
    def test_cfunctype_c_double_c_double(self):
        with open(os.devnull, 'w') as fnull:
            # These should not generate any exceptions if cffi can
            # link ctypes.CFUNCTYPE c_double, c_double to cffi.
            subprocess.call(['python', 'check_ctypes.py'], stdout=fnull, stderr=fnull)

if __name__ == "__main__":
    unittest.main()
