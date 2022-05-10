import types
types.ModuleType.__repr__ = lambda module: '<module %r version %s>' % (module.__name__, '0.0.0')


def _get_version(module, silent=True):
  version = None

  module_info = vars(module)
  config = module_info.get('config') or {}
  version = config.get('version') or config.get('__version__')
  if version:
    version = version.strip()
  else:
    if not silent:
      print '\033[93m[WARNING]\033[0m package %r did not contain any version infomation!' % module

    try:
      dirname = os.path.dirname(module.__file__)
      path = os.path.join(dirname, '../..', '..', '..', 'repo/package.json')
      with file(path, 'rb') as f:
        config = json.loads(f)
        version = config.get('version').strip()
    except Exception as e:
      if not silent:

