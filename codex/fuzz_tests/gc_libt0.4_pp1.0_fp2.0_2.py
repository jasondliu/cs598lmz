import gc, weakref
from . import _pytest._code

def _getfslineno(func):
    """ return (fslineno, fspath) of the given function. """
    code = py.code.Code(func)
    return code.fullsource

class Function(pytest._pyfuncitem.Function):
    """ base class for collecting and running test functions. """
    #: if True, the test function will be run even if it is marked with
    #: @pytest.mark.skipif
    runtest = True

    def __init__(self, name, parent=None, callspec=None, config=None,
                 keywords=None, session=None, module=None,
                 definition=None, originalname=None):
        """
        :param name: the name of the test function or a callable object.
        :param parent: the parent collector (defaults to None)
        :param callspec: a CallSpec2 object if this is a parametrized test
            function.
        :param config: pytest config object.
        :param keywords: dict of keyword values to use
