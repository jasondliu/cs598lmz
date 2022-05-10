import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [1, 2, 3]
assert fun() == [1, 2, 3]
a = fun()
assert a == [1, 2, 3]
# ____________________________________________________________
#
# PYTHONPATH
#
import sys, os
PYTHONPATHNAME = os.environ.get('PYTHONPATHNAME', 'PYTHONPATHxxx')
class AppTestSysPath:
    spaceconfig = dict(usemodules=('posix',))
    def setup_class(cls):
        cls.w_oldenv = cls.space.wrap(os.environ.copy())
        cls.w_test_support = cls.space.appexec([], """():
            import sys, test.test_support
            return test.test_support
            """)
        cls.w_save_path = cls.space.appexec([], """():
            import sys
            save_path = sys.path[:]
            del sys.path[:]
            return save_path
            """)

