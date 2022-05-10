import weakref

from . import _base
from . import _constants
from . import _util
from . import _errors


class _ParamList(object):
    """
    A list of parameters.

    This class is used to store the parameters of a function.
    """

    def __init__(self, name, parent):
        """
        Constructor.

        :param name: the name of the parameter list.
        :type name: str
        :param parent: the parent object of this parameter list.
        :type parent: :class:`_base.Function`
        """
        self._name = name
        self._parent = weakref.ref(parent)
        self._params = []

    def __repr__(self):
        """
        Return a string representation of this parameter list.

        :return: a string representation of this parameter list.
        :rtype: str
        """
        return '{}({})'.format(self.__class__.__name__,
                               ', '.join(repr(param) for param in self._params))

