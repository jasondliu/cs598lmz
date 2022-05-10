import weakref
# Test weakref.ref parametric type.
class A(object):
    pass


_wrapped_A = _g3.WeakRefType[A]

# Test mapping types (keys are always strings)
T_NUM_NUM = _g3.MappingType[int, int]
_wrapped_Mapping_NumNum = _g3.MappingType[int, int]
_wrapped_Mapping_NumFloat = _g3.MappingType[int, float]

# Call with true kwargs dict.
def kw(**kwargs):
    return kwargs


kw_wrapped = _g3.wrap_function(kw)

# Test wrapping normal class methods.

class TestClass(object):
    def get_three(self):
        return 3

    def get_three_again(self):
        return self.get_three()

    def __add__(self, other):
        if isinstance(other, TestClass):
            return TestClass()
        return NotImplemented

    @staticmethod
    def get_three_static():
        return 3


