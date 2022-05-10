import types
types.ModuleType.__repr__ = lambda module: '<module %r version %s>' % (module.__name__, '0.0.0')


def _get_version(module, silent=True):
  version = None

  module_info = vars(module)
  config = module_info.get('config') or {}
  version = config.get('version') or config.get('__version__')
  if version:
    version = version.strip()
