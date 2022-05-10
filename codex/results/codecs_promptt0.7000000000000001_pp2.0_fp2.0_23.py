import codecs
# Test codecs.register_error('ignore', codecs.ignore_errors)

import traceback

# Make sure we get the built-in threading module
import sys
if sys.modules.get('threading_dummy'):
    del sys.modules['threading']
    import threading
    

# The multiprocessing module is not (yet) a cross-platform module,
# so we need to do some platform detection here.
platform = sys.platform
darwin = (platform == 'darwin')
linux = (platform.startswith('linux'))
windows = (platform == 'win32')

if darwin:
    # On Darwin, we need to use the fork implementation
    import multiprocessing.forking as forking
else:
    # On other platforms, we use the spawn implementation
    import multiprocessing.spawn as forking

if linux or darwin:
    # We need the send_handle function on Linux and Darwin...
    import multiprocessing.connection as connection
else:
    # ... while on Windows, we need the send_handle_w function
    import multip
