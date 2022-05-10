import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    from pkg_resources import resource_filename
    def get_resource_filename(*p):
        return resource_filename('jcc', os.path.join(*p))
except ImportError:
    def get_resource_filename(*p):
        return os.path.join(os.path.dirname(__file__), *p)

def get_resource_string(filename):
    f = open(get_resource_filename(filename), 'rb')
    try:
        return f.read()
    finally:
        f.close()

def initVM(options=None, classpath=None):
    from jcc import vm
    vm.initVM(options, classpath)

def getVMEnv():
    from jcc import vm
    return vm.getVMEnv()

def shutdownJVM():
    from jcc import vm
    return vm.shutdownJVM()

def getPyJVM():
    from jcc import vm
    return vm.getPyJVM()

def attachCurrent
