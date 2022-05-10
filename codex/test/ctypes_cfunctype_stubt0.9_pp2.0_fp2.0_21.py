import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
globals()['fun'] = fun
# end pycpp issue
def get_simulator(name):
    if name == 'python':
        import python
        simulator = python
    elif name == 'pycpp':
        F = pycpp.load_extension('../build/libbrian2module')
        simulator = F.module
    elif name == 'cython':
        import Cython.build.libbrian2module
        simulator = Cython.build.libbrian2module
    else:
        raise KeyError('Unknown backend: %s' % name)

    return simulator
