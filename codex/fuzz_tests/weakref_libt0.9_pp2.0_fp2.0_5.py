import weakref
import types
import logging
import hashlib

__author__ = 'pawel'


class Parameter(object):
    """
    Class representing one configuration parameter.
    This class is used by :py:class:`.Parametrized` class.
    """

    def __init__(self, value, parameter_type, default=None, constraints=None, optional=False, label=None, description=None, helper=None,
                 controller=None, export_to=None, cache=False, info={}, order=None):
        """
        :param value: initial value for this parameter,
                      it will be checked for validity according to `constraints` and `parameter_type`
        :param parameter_type: type of parameter, i.e. :py:class:`.IntegerParameterType` or :py:class:`.Nullable`
        :param constraints: list of :py:class:`.ParameterConstraint`, :py:class:`.IntegerRangeConstraint` etc
        :param default: default value for parameter, if not provided then `value` will be used
        :param
