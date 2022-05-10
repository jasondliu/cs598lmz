import weakref
import types
import sys


class ValidateError(Exception):
    """
    Exception raised when the validation of a config fails.
    """
    pass


class Config(object):
    """
    Base class for configuration objects.
    """
    def __init__(self, **kwargs):
        """
        Initializes a configuration object.

        :param kwargs:
            Initial values for the attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def validate(self):
        """
        Validates the configuration. Raises a ValidateError if the validation
        fails.

        :return:
            ``True`` if the validation succeeds, ``False`` otherwise.
        """
        raise NotImplementedError('validate() not implemented')


