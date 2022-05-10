import gc, weakref

def _get_source_file_path():
    """
    Inspect the stack with Python's 'inspect' module
    and extract the first frame info.
    """
    frame = inspect.currentframe()
    try:
        while True:
            frame = frame.f_back
            if frame.f_code.co_filename != __file__:
                # Windows paths use backslashes, avoid escaping them:
                return frame.f_code.co_filename
    finally:
        del frame


class TestTest(unittest.TestCase):
    def setUp(self):
        # Assume the tests run from a python module ('.py')
        # Create an empty .pyo file.
        self.pyo_filename = "%s.pyo" % _get_source_file_path()
        with open(self.pyo_filename, "w") as f:
            f.write("")
        self.assertTrue(os.path.exists(self.pyo_filename))

        self.test_class = TestClass()

    def tearDown(self
