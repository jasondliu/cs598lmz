import select
# Test select.select()

while True:
    readable, writable, exceptional = select.select(
        [sys.stdin], [], [], 0.1)
    if readable:
        s = sys.stdin.readline()
        print(s)
