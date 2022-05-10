import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
globals()['fun'] = fun
globals()['ctypes'] = ctypes

def fun2(x):
    ''' Input: a list.
        Output: x, scrambled.'''
    x[0] = "HELLO"
    return x

if importlib:
    # if we have importlib, use it, otherwise we're just testing
    # cpython's #ifdef importlib
    import importlib.util
    def import_and_exec_source(filepath=TESTFN, source=TEST_SOURCE):
        file_spec = importlib.util.spec_from_loader("emit",
                                                    source_loader(source))
        m = importlib.util.module_from_spec(file_spec)
        foo = "unflushed_file"
        try:
            try:
                file_spec.loader.exec_module(m)
                return m
            finally:
                flush(foo)
        finally:
            os.unlink(filepath)
else:
    import imp
    def import_
