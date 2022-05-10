import select
# Test select.select() using stdin

print 'I/O multiplexing with select'

# wait until a key is pressed
# select returns (inputs, outputs, exceptions), all of which are lists

inputs, output, exc = select.select([sys.stdin], [], [])

# select only waits until a key is pressed.
# the inputs list is NOT the key pressed, it just tells us that a key has been pressed
# we need to read from stdin to get the key pressed
print 'got input:', sys.stdin.readline().rstrip()
