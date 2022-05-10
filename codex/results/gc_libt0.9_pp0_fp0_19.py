import gc, weakref
import logging

from pymtn import misc
from pymtn.util import obj2dict, dict2obj

__all__ = ['MutationError', 'LookupError', 'NoValueError', 'TypeError',
           'OperationNotSupportedError', 'Database',
           ]

class MutationError(Exception): pass
class LookupError(Exception): pass
class NoValueError(Exception): pass
class TypeError(Exception): pass
class OperationNotSupportedError(Exception): pass

class AttributeNotLoadedError(Exception):

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return u"%s not loaded" % self.name

    def __str__(self):
        return unicode(self).encode('utf-8')


_LOG = logging.getLogger('mtn.Database')
#_LOG.setLevel(logging.DEBUG)

class Database(object):

    STORE_UNLOADED = 0
    STORE_LOADED = 1
    STORE_LOADING = 2

   
