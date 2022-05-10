import select
# Test select.select()
#
# Usage:
#   $ python select_test.py
#   Type something:
#   <type something>
#   You typed: <what you typed>

import sys
import select

def main():
    print "Type something:"
    i, o, e = select.select( [sys.stdin], [], [], 5)
    if (i):
        print "You typed: %s" % sys.stdin.readline().strip()
    else:
        print "You said nothing!"

if __name__ == "__main__":
    main()
