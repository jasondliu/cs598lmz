import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int64, ctypes.c_int64)

# The following is necessary to be able to use the method with SWIG.
try:
    FUNTYPE.__module__ = '__main__'
except AttributeError:
    pass

# The methods of the jitclass
jitclass_methods = [(name, FUNTYPE, {}) for name in ('method1', 'method2')]

@numpy_support
class Base(object):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.x)

    @staticmethod
    def get_descriptor():
        jitclass_dict = {'x': int64[:],
                         'method1': methods['1'],
                         'method2': methods['2']}
        jitclass_struct = type('jitclass_struct', (object,), jitclass_dict)

        spec = [
            ('x', double[:]
