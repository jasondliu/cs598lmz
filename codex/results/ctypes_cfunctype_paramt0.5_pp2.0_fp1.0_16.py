import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)

def fix_path(path):
    return os.path.abspath(os.path.expanduser(path))

def find_executable(name):
    """Try to find 'name' in the directories listed in the PATH
    environment variable.  Returns the complete filename or None if not
    found
    """
    for p in os.environ['PATH'].split(os.pathsep):
        p = fix_path(p)
        fname = os.path.join(p, name)
        if os.path.isfile(fname):
            return fname
        if os.name == 'os2' and os.path.isfile(fname + ".exe"):
            return fname + ".exe"
        if os.name == 'nt' and os.path.isfile(fname + ".bat"):
            return fname + ".bat"
    return None

def get_pypath_rel():
    """Return the path to the current Python interpreter, relative
