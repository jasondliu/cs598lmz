import types
types.StringTypes

def isType(obj, flag):
    if type(flag) == types.ClassType :
        return isinstance(obj, flag)
    elif type(flag) == types.TypeType :
        return type(obj) == flag
    else :
        return 0


#
# Extend python list with default value
class ListExt(list):
    """
    Extend python list with default value
    """
    def __init__(self, default = None):
        self.default = default
        list.__init__(self)

    def __getslice__(self, i, j):
        if j - i > 0:
            return ListExt(self.default)
        else:
            return None

    def __getitem__(self, i):
        if not list.__contains__(self, i):
            list.__setitem__(self, i, self.default)
