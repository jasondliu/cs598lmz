import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
[[jit]]
def main():
    return fun()
""" In fun_linked_module.py """
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
[[jit]]
def main():
    return fun()

  @tmpdir.pyfile("mymod.pyd")
  def test_dll_funtype(self, mod_file):
    code = r"""
import fun_linked_module as othermod

[[jit]]
def main():
    return othermod.main()
"""
    mod_file.write(fun_linked_module("fun_linked_module.py"))
    mod = Script(code).compiled_module
    assert mod.main() == 42

  def test_import_py_file(self):
    """
    The builtin `import` cannot find a `.py` module. This test checks to make
    sure that the pytorch API can import it.
    """
    @tmpdir.pyfile("in1.py")
   
