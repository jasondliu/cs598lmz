import types
types.FunctionType.__call__ = types.MethodType.__call__

class Base(object):
    """
    Base class for all objects

    This class is used as the parent class for all other classes to
    provide a number of common methods.

    """

    def __init__(self, *args, **kwargs):
        """
        Loads the class attributes

        :param args: list of arguments to be loaded
        :param kwargs: list of keyword arguments to be loaded
        :return: None
        """
        # Check if the method has been overridden
        if not self.__init__.__module__ == '__main__':
            # Set the class attributes
            for attr in args:
                setattr(self, attr, None)
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        String representation of the class

        :return: string representation of the class
        """
        return str(self.__dict__)

