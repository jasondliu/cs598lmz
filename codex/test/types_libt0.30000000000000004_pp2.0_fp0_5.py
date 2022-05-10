import types
types.FunctionType = types.LambdaType

# This is a hack to get around some early `if __name__ == '__main__'` blocks
# in numpy.  It has been included in numpy 1.4.1 and later.
try:
    import __builtin__ as builtins
except ImportError:
    import builtins
builtins.__NUMPY_SETUP__ = False
import numpy

from numpy.distutils.core import setup

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('pyemma')
    config.add_data_dir('pyemma/tests')

    return config

