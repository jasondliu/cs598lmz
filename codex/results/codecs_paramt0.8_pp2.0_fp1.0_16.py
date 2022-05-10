import codecs
codecs.register_error('strict', codecs.lookup_error('strict'))
codecs.register_error('ignore', codecs.lookup_error('ignore'))

try:
    import scipy
except ImportError:
    msg = "Required module 'scipy' not found. Please install it via 'conda'" + \
            "or 'pip' prior to the installation of 'notebook'"
    raise ImportError(msg)
try:
    import numpy
except ImportError:
    msg = "Required module 'numpy' not found. Please install it via 'conda'" + \
            "or 'pip' prior to the installation of 'notebook'"
    raise ImportError(msg)
try:
    import pandas
except ImportError:
    msg = "Required module 'pandas' not found. Please install it via 'conda'" + \
            "or 'pip' prior to the installation of 'notebook'"
    raise ImportError(msg)
try:
    import ipywidgets
except ImportError:
    msg = "Required module 'ipywidgets'
