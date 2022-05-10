import gc, weakref

from   _Gripper import Gripper


def _ref_gripper (self):
    if self.__id is None:
        self.__id = self.__id_gen.next ()
    return self.__id

def _del_gripper (self, wr = weakref.ref):
    try:
        del self.__id
    except AttributeError:
        pass
    else:
        self = wr (self, _del_gripper)
        wr   (self, _ref_gripper)
        gc.collect  ()

class _Ref_Gripper (Gripper):

    def __init__ (self, obj):
        Gripper.__init__ (self, obj)
        self.__id_gen  = itertools.count ()
        self.__id      = None
        self.__ref     = weakref.ref (self, _del_gripper)

    def __repr__ (self):
        return "<%s #%d>" % (self.__class__.__name__, _
