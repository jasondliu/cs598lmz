import weakref
import functools
from mtk.tools import SafeWrapper

__all__ = ['JsonObject']

class JsonObject(object):
    '''JsonObject - Json Object class
    
    :param string contents: The contents that used to init JsonObject
    
    :param dict dict_obj: The dict that used to init JsonObject
    '''
    def __init__(self, contents=None, dict_obj=None):
        self._parent = None
        self._objs = set()
        self._dict = {}
        self._value = None
        if contents is not None and dict_obj is None:
            dict_obj = json.loads(contents)
        if dict_obj is not None:
            self._dict = dict_obj
            for k,v in self._dict.iteritems():
                if isinstance(v, dict):
                    self._objs.add(k)
            self._objs = set(self._dict.keys())

    def __str__(self):
        return self._to_string(self, 0
