import types
types.__dict__['type']

# Reload manually
reload(f_module) # f_module is that module, not the f().
reload(__import__('f_module'))
imp.reload(sys.modules['f_module'])
eval('import f_module')


# PYTHONPATH
os.env['PYTHONPATH'] = '';  # modify
sys.path = [];  # manipulate
sys.path.append("path")
sys.path.insert(0, "path")
sys.path.insert(0, '')
sys.path.insert(0, os.curdir)
sys.path.insert(0, os.pardir)
sys.path.insert(0, os.path.expanduser('~/lib/python'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# reload Module
def reload_package(packagename):
  import imp
  import sys
  import os

  rootdir = os.path.
