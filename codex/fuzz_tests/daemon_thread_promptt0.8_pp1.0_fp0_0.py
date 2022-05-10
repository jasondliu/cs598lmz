import threading
# Test threading daemonic threads
import _thread
if hasattr(threading, "main_thread"):
    main_thread = threading.main_thread
else:
    main_thread = None
import os

import test.support
# Skip test if _thread is not available.
test.support.import_module("_thread")

# If threading is available, test_main() should be invoked by
# test_support.run_unittest()
test.support.run_unittest(ThreadTests)

# Test that Daemonic threads will exit when their parent does.
if 0:
    def main():
        test.support.verbose = 1
        if len(sys.argv) > 1:
            # child process
            print("Child: daemonic is", threading.current_thread().daemon)
            exit_code = not int(sys.argv[1])
            exit_code_2 = not exit_code
            sys.exit(exit_code)
        else:
            # parent process
            import subprocess
            print("Main: daemonic is", threading.
