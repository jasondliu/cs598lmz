import types
types.ModuleType.__repr__ = lambda self: self.__name__
import sys
#sys.meta_path.append(importlib.import_module('lib.hook', 'Jython'))
sys.meta_path.append(importlib.import_module('lib.hook'))

from lib.hook.hook_sys_meta_path import HookSysMetaPath
hook_meta_path = HookSysMetaPath()
hook_meta_path.uninstall()
hook_meta_path.install()

import sys
import types
ModuleType = types.ModuleType
f = sys.meta_path.pop(-1)
class JythonImporter():
    """Metapath importer for jython"""
    def __init__(self, hook_meta_path, hook_dict=None):
        self.hook_meta_path = hook_meta_path
        if hook_dict is not None:
            hook_dict['__mp'] = self
        self.hook_dict = hook_dict
        self.module = ModuleType('JythonImporter')
