import types
types.ModuleType.__getitem__ = __getitem__
types.ModuleType.__setitem__ = __setitem__

# load the config file
execfile("../conf/config.py")

# redefine a few things
config['source_directories'] = ["../src/"]
