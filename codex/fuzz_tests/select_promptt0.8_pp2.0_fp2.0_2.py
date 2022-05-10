import select
# Test select.select() using stdin

print('Please enter and EOF to exit.')

while True:
    ready, _, _ = select.select([sys.stdin], [], [])
    if ready:
        line = sys.stdin.readline()
        if not line:
            break
        print('Input:', line)
    else:
        print('No input yet')

print('All done')
