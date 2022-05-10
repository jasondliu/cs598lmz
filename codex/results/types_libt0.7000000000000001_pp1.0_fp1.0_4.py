import types
types.MethodType = MethodType

class Object(object):
    """
    Non-descript class for doing generic operations.  It is just a
    container for functions and data.
    """

    def __init__(self, **kwd):
        """
        Create a new Object.  See the _init_defaults method for
        the allowed parameters.
        """
        self._init_defaults(**kwd)

    def _init_defaults(self, **kwd):
        """
        Initialize the object with the keyword parameters in dictionary
        'kwd'.
        """
        pass

    def copy(self, deep=False):
        """
        Create a copy of the object.

        Parameters
        ----------
        deep : bool
            Flag indicating whether to make a deep copy or not.
        """
        return copy.copy(self)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        return self.copy(deep=True)

    def get_id(self):
        """
        Return an
