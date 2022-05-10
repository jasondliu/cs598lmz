import select
# Test select.select() using stdin

while True:
    readable, writable, exceptional = select.select([sys.stdin], [], [])
    for s in readable:
        if s is sys.stdin:
            print sys.stdin.readline()
