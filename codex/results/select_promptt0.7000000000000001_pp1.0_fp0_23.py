import select
# Test select.select()
import time

def wait_for_something(msecs):
    """Wait for input on stdin or until timeout.

    Arguments:
    msecs -- Timeout in milliseconds

    Return value:
    True if input available, False on timeout
    """
    # Build the timeout into a list so we can modify it
    timeout = [msecs / 1000.0]
    print("Waiting for %s seconds on stdin..." % timeout[0])
    (rlist, wlist, xlist) = select.select([sys.stdin], [], [], timeout)
    print("Waited for %s seconds." % timeout[0])
    # If rlist is not empty, something is available for reading
    return (rlist != [])

def main():
    if len(sys.argv) == 2:
        msecs = int(sys.argv[1])
    else:
        msecs = 1000
    while True:
        if wait_for_something(msecs):
            print("Something!")
        else:
            print("Nothing!")

