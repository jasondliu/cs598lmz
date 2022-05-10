fn = lambda: None
# Test fn.__code__.co_filename fails in Python 2.5
def test_fn(): pass

def get_relative_path(full_path):
    """Return the relative path from the root directory to the given file.
    """
    assert full_path.startswith(BASE_DIR)
    path = full_path[len(BASE_DIR):]
    if path.startswith(os.sep):
        path = path[len(os.sep):]
    return path


def get_module_name(module_path):
    """Return the module name of a given module path.
    """
    assert module_path.endswith('.py')
    return module_path[:-3].replace(os.sep, '.')


def get_module_path(module_name):
    """Return the module path of a given module name.
    """
    return '%s.py' % module_name.replace('.', os.sep)


def import_module(module_name, path=None):
    """Import and return a module.
    """
