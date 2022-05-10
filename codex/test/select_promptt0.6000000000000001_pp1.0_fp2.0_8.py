import select
# Test select.select() for a specific timeout.

import sys
import os
import select
import time

def test_select(timeout):
    if timeout is None:
        result = select.select([sys.stdin], [], [])
    else:
        result = select.select([sys.stdin], [], [], timeout)
    return result

def test_select_with_exception(timeout):
    if timeout is None:
        try:
            result = select.select([sys.stdin], [], [])
        except select.error as e:
            print("select.select() raised %s" % e)
            return None
    else:
        try:
            result = select.select([sys.stdin], [], [], timeout)
        except select.error as e:
            print("select.select() raised %s" % e)
            return None
    return result

def main():
    if os.name == "nt":
        print("skipping test on Windows")
        sys.exit(0)

    print("Testing select.select() with no timeout")

