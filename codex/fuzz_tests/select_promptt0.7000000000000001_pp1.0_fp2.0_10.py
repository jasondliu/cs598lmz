import select
# Test select.select() using STDIN file object, stdin.
import sys

while True:
    readable, w, x = select.select([sys.stdin], [], [], 0.0)
    if readable:
        s = sys.stdin.readline()
        # Print as you type
        print("You typed", s)
        if s == "\n":
            break
    else:
        print("No input. Moving on.")
