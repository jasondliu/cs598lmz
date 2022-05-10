import select
# Test select.select

import select
import socket

def test(args=None, msg=None):
    if msg is not None: print(msg)
    try:
        r, w, x = select.select(*args)
    except select.error as err:
        print("Error: %s" % err)
    else:
        print("OK:", r, w, x)

print("Testing bad file objects...")

# Try a bad file object
bad_file = socket.socket()
bad_file.close()

test(args=([bad_file], [], []),
     msg="Expect an error with a closed file object")

# Now a bad file number
test(args=([42], [], []),
     msg="Expect an error with a bad file number")

print("Testing bad timeouts...")

# Try a bad timeout
test(args=([], [], []),
     msg="Expect an error with a negative timeout")

# Try a bad timeout
