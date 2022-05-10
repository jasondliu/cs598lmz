import select
# Test select.select

import select
import sys
import time

def main():
    # monitor stdin and stdout
    rlist = [sys.stdin, sys.stdout]
    wlist = []
    xlist = []

    while True:
        # block until input is available
        rl, wl, xl = select.select(rlist, wlist, xlist)
        print("rl = %r" % rl)
        print("wl = %r" % wl)
        print("xl = %r" % xl)
        # stdout is available for write
        if sys.stdout in wl:
            sys.stdout.write("stdout is available for write\n")
            sys.stdout.flush()
            wlist = []
        # stdin is available for read
        if sys.stdin in rl:
            s = sys.stdin.readline()
            if not s:
                break
            sys.stdout.write("read: %s" % s)
            sys.stdout.flush()
            rlist = []
