import ctypes
# Test ctypes.CFUNCTYPE capabilities
# - adding keywords
# - passing non standard args
# - checking return values

specials = {'int_np': {'flags': 'NPY_ARRAY_FORCECAST | NPY_ARRAY_UPDATEIFCOPY'},
            'float_np': {'flags': 'NPY_ARRAY_FORCECAST | NPY_ARRAY_UPDATEIFCOPY'},
            'complex_np': {'flags': 'NPY_ARRAY_FORCECAST | NPY_ARRAY_UPDATEIFCOPY'},
            'int_np2': {'flags': 'NPY_ARRAY_FORCECAST | NPY_ARRAY_UPDATEIFCOPY | NPY_ARRAY_IN_ARRAY'},
            'float_np2': {'flags': 'NPY_ARRAY_FORCECAST | NPY_ARRAY_UPDATEIFCOPY | NPY_ARRAY_IN_ARRAY'},
            'complex_np2': {'flags': 'NPY_ARRAY_FORCECAST | NPY_AR
