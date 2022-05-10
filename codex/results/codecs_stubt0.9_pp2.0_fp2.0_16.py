import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class TestBase(BaseTestCheck):
    # check the expected error message in python code running on the py2.7
    # interpreter
    test_check_output_py = import_module(".data.check_output_py", "language_tags")
    assert isinstance(test_check_output_py, types.ModuleType)

    @unittest.skipUnless(
        (sys.version_info > (2, 7)) and (sys.version_info < (3, 0)),
        "requires Python 2.7"
    )
    def test_check_output_py(self):
        #### run the check.py code
        errno = subprocess.call([executable, self.test_check_output_py.__file__],
                                cwd=None,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        self.assertEqual(errno, 1, "check.py should exit with error")

        #### check the error message in stderr file
        err_msg = self.st
