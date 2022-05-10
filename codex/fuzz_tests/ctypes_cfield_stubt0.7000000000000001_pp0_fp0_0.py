import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test_annotation(BaseTestChecker):
    CHECKER_CLASS = _testcapi.cfield_annotation
    def test_check_annotation(self):
        assert self.CHECKER_CLASS.check_annotation(S.x) == 1
        assert self.CHECKER_CLASS.check_annotation(S.x) == 1
        assert self.CHECKER_CLASS.check_annotation(ctypes.CField) == 1

# _testcapi.cfield_annotation_warn is the same as _testcapi.cfield_annotation,
# but it generates a warning
