import select
# Test select.select() with file descriptors in a list and a small timeout
import os
import unittest


def test_subprocess(subprocess):
    rfd, wfd = os.pipe()
    rf = os.fdopen(rfd)
    wf = os.fdopen(wfd, 'w')

    p = subprocess.Popen([sys.executable, '-c',
                   """if 1:
                      import sys, time
                      time.sleep(1)
                      print('x')
                      sys.stdout.flush()
                   """],
                   stdin=subprocess.PIPE,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    try:
        # Wait for the subprocess to start.
        select.select([rfd], [], [])
        wf.close()
        rv = select.select([p.stdout], [], [], 0.1)
        if rv == ([], [], []):
            # Select reported no data at all, not even the child exit status.
           
