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

