import select
# Test select.select() and select.poll() for pause() and wait() methods

from test.support import run_unittest, import_module, verbose, reap_threads
import time, sys, errno

# Skip test if there is no select module.
select = import_module('select')

# These tests are only appropriate for Unix; skip them under IronPython.
if sys.platform == 'cli':
    raise unittest.SkipTest('select tests not appropriate for IronPython.')

#
# Make sure you can use select.poll() or just select.select() to put a
# Thread in a paused state.
#

class Subclass(threading.Thread):

    def __init__(self):
        # This file descriptor is used simply as a way to pause the thread
        self.read_fd, self.write_fd = os.pipe()
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            while not self.paused:
                time.sleep(1)
            self.enter_paused_state()
