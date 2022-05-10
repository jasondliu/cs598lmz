import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.py_object, ctypes.c_char_p)

def add_to_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

def load_module(modname, path, *args):
    add_to_path(path)
    mod = __import__(modname, globals(), locals(), [], -1)
    return mod.CModule(*args)

def load_module_from_file(modname, filepath, *args):
    path = os.path.dirname(filepath)
    modname = os.path.splitext(os.path.basename(filepath))[0]
    return load_module(modname, path, *args)

def load_module_from_spec(spec, *args):
    modname = spec.name
    path = spec.submodule_search_locations[0]
    return load_module(modname, path, *args)

def load_module_from_file_
