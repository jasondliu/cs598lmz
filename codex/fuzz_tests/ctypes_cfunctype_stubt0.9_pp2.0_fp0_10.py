import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return range(10)
'''
        self.assertTrue(self.check_import_to_c(m, target))

    def test_import_funtype_pyobject_args(self):
        """Test the last case funtype(pyobjects, ...)"""
        for args in ['()', '(ctypes.py_object, ctypes.py_object)', '([object, object], [object, object])']:
            m = '''\
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, %s)
@FUNTYPE
def fun():
  return range(10)
''' % args
            self.assertTrue(self.check_import_to_c(m, target))


class Test_PyObject_fget(TestInterpreterMixin, unittest.TestCase):
    def test_fget_same_type(self):
        """Tests `ctypes.PyObject.fget`"""
        m = '''\
import ctypes

def set_attribute(obj, value, attribute='attribute
