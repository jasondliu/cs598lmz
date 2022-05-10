import io
# Test io.RawIOBase
class RawIOTest(BaseTestChecker):
    CHECKER_CLASS = methods.RawIOBaseChecker

    def test_rawio_methods(self):
        input_str = """
class TestRawIO(io.RawIOBase):
    def read(self):
        pass
    def readinto(self):
        pass
    def write(self):
        pass
"""
        tree = test_utils.build_ast_from_str(input_str)
        rawio_cls = tree.body[0]

        checker = self.get_checker(rawio_cls)
        checker.visit(rawio_cls)

        assert self.error_in_log() == 0


    def test_missing_method_read(self):
        input_str = """
class TestRawIO(io.RawIOBase):
    def readinto(self):
        pass
    def write(self):
        pass
"""
        tree = test_utils.build_ast_from_str(input_str)
        rawio_cls =
