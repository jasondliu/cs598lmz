import types
types.ClassType
types.TypeType

import inspect, types
def isclass(object):
    return isinstance(object, (types.ClassType, types.TypeType))

