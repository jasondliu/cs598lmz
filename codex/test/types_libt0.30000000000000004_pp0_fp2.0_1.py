import types
types.ModuleType.__init__ = types.ModuleType.__init__

from . import _pytest

# pytest.main() must be called from a module, so we need to create a dummy
# module to call it from.
class _PytestPluginModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.__file__ = __file__


_pytest_plugin_module = _PytestPluginModule('_pytest_plugin_module')

# We need to call pytest.main() from a module, so we need to create a dummy
