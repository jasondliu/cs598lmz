import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
</code>
EDIT:
<code>from cStringIO import StringIO
from threading import Thread

def thread_output(callable, output):
    """
    Run `callable`, capture its output to `output` (a file-like object).
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    try:
        sys.stdout = output
        sys.stderr = output
        callable()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

def main():
    # create file-like object to capture output
    output = StringIO()
    # start thread and pass it the callable to be run, as well as the output
    # object
    Thread(target=lambda: thread_output(lambda: sys.stdout.write("hello\n"),
                                         output)).start()
    # print the captured output after a short delay
    import time
    time.sleep(
