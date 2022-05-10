import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "Called"
    return 'ni'

def init():
    pyci.pyci_ninitialize()
    mu = pyci.pyci_mu()
    sys.stdout = sys.stderr
    return mu

def finalize():
    pyci.pyci_nfinalize()


def test_c_flags():
    mu = init()
    pyci.pyci_set_c_flags(mu, "-I include")
    assert pyci.pyci_c_flags(mu) == "-I include"
    finalize()


def test_cpp_flags():
    mu = init()
    pyci.pyci_set_cpp_flags(mu, "-I include")
    assert pyci.pyci_cpp_flags(mu) == "-I include"
    finalize()


def test_ld_flags():
    mu = init()
    pyci.pyci_set_ld_flags(mu, "-Wl")
    assert pyci.pyci_ld_flags(mu) == "-Wl"
    finalize()
