import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 12345

def setup_module(mod):
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestCase(unittest.TestCase):

    def test_funcs(self):
        import pypy.module.cppyy.capi as cppyy

        cls = cppyy.gbl.std.vector[int]

        # cppyy.py is OK
        assert cppyy.gbl.gROOT is not None
        assert cppyy.gbl.gROOT.FindObject("TInterpreter") is not None

        # test default value, which can be any type
        assert cppyy.gbl.gROOT.GetMacroPath() == ".:/u/lbechtel/software/installed/root/5.34-python2.7.6-gcc/lib/root"
        assert cppyy.gbl.gROOT.GetEditorMode() == 111
