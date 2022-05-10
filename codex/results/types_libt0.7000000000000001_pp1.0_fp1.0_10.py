import types
types.FunctionType = types.ClassType

def add_to_path(path):
    if path not in sys.path:
        sys.path.insert(1, path)

add_to_path('/home/david/PycharmProjects/pymol-open-source/modules/pymol/contrib/')

# Path to the PyMOL source code
pymol_path = '/home/david/PycharmProjects/pymol-open-source'

# Path to the PyMOL source code
add_to_path(pymol_path)

# Path to the PyMOL shared libraries
add_to_path('%s/modules' % pymol_path)

# Path to the PyMOL submodules
add_to_path('%s/modules/pymol' % pymol_path)

# Path to the PyMOL submodules
add_to_path('%s/modules/pymol/contrib' % pymol_path)

# Path to the PyMOL submodules
add_
