import ctypes
import ctypes.util
import threading
import sqlite3

import logging
log = logging.getLogger(__name__)

# We need to import clang.cindex manually, as we can't rely on it having
# been installed.
def import_clang():
    import os
    import sys
    import imp
    import inspect

    # Check if clang.cindex is installed.
    # TODO: It would be good to check the actual version.
    try:
        import clang.cindex
        return
    except ImportError:
        pass

    # On Linux, we will attempt to load a bundled version of libclang.
    if sys.platform.startswith("linux"):
        if sys.maxsize > 2**32:
            libclang_name = "libclang.so.3.6"
        else:
            libclang_name = "libclang.so.3.6"

        libclang_path = os.path.join(
            os.path.dirname(inspect.getabsfile(import_clang)),
            "libclang.so.3.6")
