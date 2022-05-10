import select
# Test select.select() using stdin

# Register the socket to receive data
inputs = [sys.stdin]

# Loop until something is received
while True:
    readable, writable, exceptional = select.select(inputs, [], [])

    for s in readable:
        if s is sys.stdin:
            c = sys.stdin.read(1)
            sys.stdout.write(c)
            sys.stdout.flush()
