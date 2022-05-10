gi = (i for i in ())
# Test gi.gi_code
class TestCodeObjectAsFunctionArgumentC(BaseTestCheckCodeObject):
    def test_code_object_as_function_argument_c0(self):
        self._check_code_object('''def x(): return 1
def y(a): return lambda: x() + a
print(y(2)())''', '3', gi)

    def test_code_object_as_function_argument_c1(self):
        self._check_code_object('''def x(): return 1
def y(a, b): return lambda: x() + b + a
print(y(2, 3)())''', '6', gi)

    def test_code_object_as_function_argument_c2(self):
        self._check_code_object('''def x(): return 1
def y(a, b, c): return lambda: x() + b + c + a
print(y(2, 3, 4)())''', '10', gi)

    def test_code_object_as_function_argument_c3(self):
       
