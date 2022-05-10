import _struct
import _struct as struct
import sys
import threading
import time
import traceback
import types
import warnings

from _weakrefset import WeakSet

# The following is a hack to get around the fact that the
# _thread module doesn't expose the _local class.
_local = _thread._local

# The following is a hack to get around the fact that the
# socket module doesn't expose the _fileobject class.
_fileobject = socket._fileobject

# The following is a hack to get around the fact that the
# socket module doesn't expose the _closedsocket class.
_closedsocket = socket._closedsocket

# The following is a hack to get around the fact that the
# socket module doesn't expose the _delegate_methods class.
_delegate_methods = socket._delegate_methods

# The following is a hack to get around the fact that the
# socket module doesn't expose the _realsocket class.
_realsocket = socket._realsocket

# The following is a hack to get around the fact that the
# socket module doesn't expose the
