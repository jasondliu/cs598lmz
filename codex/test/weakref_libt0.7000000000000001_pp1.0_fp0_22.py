import weakref

from synapse.event_lib import Event
from synapse.exc import SynErr
from synapse.common import *

class FormProp:
    '''
    Base class for all Form properties.
    '''
    def __init__(self, valu=None, **info):
        self.valu = valu
        self.info = info

    def repr(self):
        return s_common.reprlib.repr(self.valu)

    def repr_full(self):
        return repr((self.valu,self.info))

class FormPropMeta(type):
    '''
    Metaclass for FormProp instances.  All FormProps have a name
    property and a type name property.  This metaclass sets those
    based on the class name.
    '''
    def __init__(self, name, bases, dict):
        type.__init__(self, name, bases, dict)
        self.name = name.lower()
        self.typen = name.lower()

