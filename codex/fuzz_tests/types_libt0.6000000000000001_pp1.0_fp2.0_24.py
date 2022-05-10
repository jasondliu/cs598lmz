import types
types.ModuleType.__getattr__ = lambda self, key: types.ModuleType(key)

# import sys
# import types
# from types import ModuleType
#
# __all__ = ['ModuleType', 'ModuleType', 'ModuleType']
#
#
# def _getattr(self, key):
#     return ModuleType(key)
#
#
# ModuleType.__getattr__ = _getattr
# sys.modules[__name__] = ModuleType(__name__)
#
# sys.modules[__name__].__getattr__ = _getattr

# def _getattr(self, key):
#     return ModuleType(key)
#
#
# ModuleType.__getattr__ = _getattr
