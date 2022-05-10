import types
types.ModuleType

try:
    import cPickle as pickle
except ImportError:
    import pickle

from waflib import Utils, Logs, Configure, Options, Build
from waflib.Configure import conf
from waflib.TaskGen import feature, before_method, after_method, extension
from waflib.Errors import WafError
from waflib.Task import Task, ASK_LATER
from waflib.Tools import c_preproc

from waflib.Tools.compiler_c import c_compiler
from waflib.Tools.compiler_c import cxx as cxx_compiler

import waflib.Tools.c_osx
import waflib.Tools.c_config

# ------------------------------------------------------------
# utility methods
# ------------------------------------------------------------
