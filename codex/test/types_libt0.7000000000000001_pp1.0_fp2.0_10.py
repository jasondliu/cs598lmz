import types
types.ModuleType('__builtin__').__dict__['__import__'] = my_import

import test_import

