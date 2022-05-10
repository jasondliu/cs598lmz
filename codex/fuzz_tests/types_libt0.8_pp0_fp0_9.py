import types
types.ModuleType.__getitem__ = __getitem__
types.ModuleType.__setitem__ = __setitem__

# load the config file
execfile("../conf/config.py")

# redefine a few things
config['source_directories'] = ["../src/"]
config['libraries'] = ["stdc++", "xml2", "pthread", "bz2", "dl", "rt",
                       "gc-libcordoba", "gc-thread_local", "gc-main",
                       "gcc-eh", "supc++", "gcj_bc", "gcj", "gcj_support",
                       "gcjaot", "gcjgi", "gcjgc", "gij", "gcc-s", "gcc",
                       "unwind", "m", "gc-redirects", "gc-redirects-gcc",
                       "gc-gcj", "gc-oldmalloc", "objc-unwind", "gcc_eh",
                       "gc-gcj-support", "gc-gcj-support-gcc",
