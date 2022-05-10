import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() with the 'uri=true' option.
#
# The default is to accept only URIs with an authority section.
#
# This test uses the 'uri=true' option to accept URIs without
# an authority section.
#
# NOTE: This test should not be run in parallel with other tests,
# as it changes the global sqlite3.enable_shared_cache setting.

#------------------------------------------------------------------------------
# The test logic.

def test_uri_true():
    """
    Test sqlite3.connect() with the 'uri=true' option.

    The default is to accept only URIs with an authority section.

    This test uses the 'uri=true' option to accept URIs without
    an authority section.

    NOTE: This test should not be run in parallel with other tests,
    as it changes the global sqlite3.enable_shared_cache setting.
    """
    # NOTE: This test should not be run in parallel with other tests,
    # as it changes the global sqlite3.enable_shared_cache setting.
    #
    # The shared cache must be disabled, because this
