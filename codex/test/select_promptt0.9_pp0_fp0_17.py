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
