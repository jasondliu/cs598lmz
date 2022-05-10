import mmap
import os
import re
import sys

from . import _compat
from . import _util
from . import _winreg
from . import _winreg_util

_log = logging.getLogger(__name__)

_REG_SZ = 1
_REG_EXPAND_SZ = 2
_REG_BINARY = 3
_REG_DWORD = 4
_REG_MULTI_SZ = 7
_REG_QWORD = 11

_REG_OPTION_BACKUP_RESTORE = 0x00000004
_REG_OPTION_OPEN_LINK = 0x00000008

_REG_OPEN_SUBKEY_FAIL_IF_NEW = 0x00000001
_REG_CREATED_NEW_KEY = 0x00000001
_REG_WHOLE_HIVE_VOLATILE = 0x00000001
_REG_REFRESH_HIVE = 0x00000002
_REG_NO_LAZY_FLUSH = 0x00000004
_REG_NOTIFY_CHANGE_NAME = 0x00000001
_
