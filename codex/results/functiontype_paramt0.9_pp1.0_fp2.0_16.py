from types import FunctionType
list(FunctionType(1, 2, 3, 4, 5, 6, 7, 8, closed_over_variable=9))
""")


class RedefinitionTests(PydevTestCase):

    def test_class_redefinition(self):
        self.check_invalid_syntax("""
class C(object):
    def m1(self):
        pass

    def m2(self):
        pass

class C(object):
    def __init__(self):
        pass

    def m2(self):
        pass
""")

        self.check_invalid_syntax("""
class C(object):
    pass

class C:
    pass
""")

        self.check_valid_code("""
from types import FunctionType
def m1(self):
    pass
def m2(self):
    pass

class C(object):
    __init__ = FunctionType(m1, 1, 2, 3, 4, 5, 6, 7, closed_over_variable=9)
    f = FunctionType(m2, 1, 2, 3
