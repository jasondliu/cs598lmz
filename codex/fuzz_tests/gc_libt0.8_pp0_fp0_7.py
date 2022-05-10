import gc, weakref
from clink.iface import IFace
from clink.type import get_type, TypeInfo

class UndefineException(Exception):
    '''Undefine exception'''
    pass


class Proxy(object):
    '''
    Proxy object

    >>> p = Proxy(IFace)
    >>> p.tag
    >>> p.tag = 'proxy'
    >>> p.tag
    'proxy'
    '''

    __slots__ = ('__co__', '__cls__', '__refs__', 'tag')

    def __init__(self, iface):

        self.__cls__ = get_type(iface)
        self.__refs__ = weakref.WeakKeyDictionary()
        self.__co__ = None

        # set attr on self
        type_list = self.__cls__.values()
        proxy_dict = self.__dict__

        for tp in type_list:
            self.__refs__[tp.name] = None
            # set auto handle attr or func
            if
