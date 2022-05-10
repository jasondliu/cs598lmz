import _struct
import types

class DictInfo :
    def __init__(self) :
        self.key_info   = []
        self.value_info = []

    def setup(self, key_info, value_info) :
        self.key_info   = key_info
        self.value_info = value_info

class AttributeInfo :
    def __init__(self) :
        self.name = ''
        self.type = ''
        self.type_info = {}
        self.len = 0
        self.c_type = ''
        self.desc = ''

def _get_structure(ttype, tname, name) :
    if tname == 'aDictionary' :
        return DictInfo()
    elif tname == 'aData' :
        return AttributeInfo()
    else :
        return types.SimpleNamespace()

def _get_sublist(lst, prefix) :
    return [x for x in lst if x.startswith(prefix)]

def _get_dict(info, pr
