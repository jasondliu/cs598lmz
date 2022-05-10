import select
# Test select.select() using stdin

print('Please enter your name: ')

while True:
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        name = sys.stdin.readline().strip()
        break
    print('Please enter your name: ')

print('Hello, {}'.format(name))
