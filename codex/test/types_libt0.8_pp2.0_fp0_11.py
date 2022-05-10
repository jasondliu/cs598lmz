import types
types.FunctionType = type(lambda x:x)
types.MethodType = type(lambda x:x)
types = None

#
# Import MySQLdb as _mysql
#
import _mysql

# for pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

# for datetime
try:
    import datetime
except ImportError:
    raise _mysql.NotSupportedError("Python 2.3 or higher is required")

# for warnings
import warnings
if hasattr(sys, "py3kwarning"):
    warnings.filterwarnings("default", ".*", Warning, "MySQLdb")

# vars of MySQLdb
version_info = (1, 2, 3, "final", 0)
__revision__ = "$Revision: 1.50 $"[11:-2]
# version_info.__init__(1, 2, 4, "beta", 4)
# __revision__ = "$Revision: 1.51 $"[11:-2]
# client_info = "Python MySQLdb " + __version__
