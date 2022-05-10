import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Helper functions
#
#------------------------------------------------------------------------------

def get_module_path(module):
    """ Returns the path to the given module.

    Parameters
    ----------
    module : module
        The module to get the path of.

    Returns
    -------
    path : str
        The path to the given module.

    """
    return os.path.dirname(module.__file__)

def get_module_data_path(module, relpath=None, attr_name='DATAPATH'):
    """ Returns the path to a data directory of the given module.

    Parameters
    ----------
    module : module
        The module to get the data path of.
    relpath : str
        The path of the data directory with respect to the module path.
    attr_name : str
        The name of the module attribute which should be checked first for the
        path.

    Returns
    -------
    path : str
        The path to the data directory of the given module.

    """

