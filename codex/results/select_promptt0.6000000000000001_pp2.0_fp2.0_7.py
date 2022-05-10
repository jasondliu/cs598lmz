import select
# Test select.select()
while True:
    readable, writable, exceptions = select.select([sys.stdin], [], [])
    if sys.stdin in readable:
        print(sys.stdin.readline())
