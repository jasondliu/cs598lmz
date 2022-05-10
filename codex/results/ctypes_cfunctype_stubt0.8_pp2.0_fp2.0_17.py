import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

'''Error already raised in ffi:e: error: '+' not supported between instances of
'_ctypes.PyCFuncPtrType' and 'str'''

os.environ['PYPY_USESSION_DIR'] = '/tmp/usession_' + str(os.getuid())
# using fork() instead of some subprocess stuff which may be affected by
# Python environment variables
#
pid = os.fork()
if pid == 0:
    # child process
    from pypy.module.cpyext.test.test_api import option
    option.usemodules = ['array'] + option.usemodules
    try:
        os.execvp('pypy', ['pypy', '--translation-jit_opencoder_model=big',
            '--translation-jit_opencoder_model=big',
            '-Ojit', '--heapsize', '512m',
            '-c', 'import cpyext.bench; cpyext.bench.run()'])
    finally:
        os._exit(1)
else
