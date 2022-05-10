import gc, weakref

#==============================================================================
# Copy a list of instances, without copying the instances.
#==============================================================================

class ReferenceList(list):
    def append(value):
        super(ReferenceList, self).append(weakref.ref(value))

    def __getitem__(value):
        return super(ReferenceList, self).__getitem__(weakref.ref(value))

#==============================================================================
# A class instance which automatically releases its reference to a list
#==============================================================================

class KeepInList:
    COUNT = 0

    @classmethod
    def Cleanup(name, count=10):
        if COUNT >= count:
            list = gc.get_referrers(KeepInList)
            for item in list:
                if isinstance(item, list) and item in item:
                    item.remove(item)
                COUNT = 0

    @classmethod
    def Get(cls, name):
        for list in gc.get_referrers(cls):
            for item in list:
                if item.NAME == name:
                    return
