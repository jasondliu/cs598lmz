import select
# Test select.select()
import sys
import time

# Wait for input on stdin and stdout

while True:
    readable, writable, exceptional = select.select(
        [sys.stdin], [], [], 1.0)
    if not (readable or writable or exceptional):
        print('  Timeout')
    for s in readable:
        if s is sys.stdin:
            input = sys.stdin.readline()
            print('Input:', repr(input))
            if not input:
                print('(Exit)')
                sys.exit()
