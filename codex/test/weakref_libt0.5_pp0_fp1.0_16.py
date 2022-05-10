import weakref

from . import helpers
from . import validator
from . import exceptions
from . import constants


class BaseField(object):
    """
    Base field class.

    :param str name: Name of the field.
    :param bool required: Whether the field is required or not.
    :param callable default: Default value for the field.
    :param callable validator: Validator function.
    :param callable pre_set: Function to be called before the field is set.
    :param callable post_set: Function to be called after the field is set.
    :param callable pre_get: Function to be called before the field is get.
    :param callable post_get: Function to be called after the field is get.
    :param bool read_only: Whether the field is read only or not.
    :param str doc: Field docstring.
    """

