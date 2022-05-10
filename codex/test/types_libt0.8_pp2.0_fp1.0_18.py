import types
types.__doc__ = ''
types.__all__ = ['NoneType', 'ModuleType', 'TypeType', 'ObjectType', 'TracebackType']

import sys
if sys.version_info[0] > 2:
    types.ModuleType = module
