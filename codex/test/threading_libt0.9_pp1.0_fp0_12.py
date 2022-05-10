import threading
threading.get_ident()

# Try to catch a segmentation fault in a child process
# and let the parent handle it too, so the threads itself
# don't abort
import threading

class Killable(threading.Thread):
    def run(self):
        while True:
            object()

def let_parent_catch_segfault():
    threading.Thread(target=Killable().start,
                     daemon=True).start()

try:
    import subprocess
    subprocess.check_call(
        ["python3.3", "-c",
         "import sys; sys.path[0:0] = ['.']; "
         "import test_threading; "
         "test_threading.let_parent_catch_segfault()"],
        stderr=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    if b'segfault' in e.stderr:
        # this is good for us,
        # the child process crashed
        pass
    else:
        raise

# Issue #
