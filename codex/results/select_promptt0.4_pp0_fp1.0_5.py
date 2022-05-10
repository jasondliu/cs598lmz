import select
# Test select.select

def test(readable, writable, exceptional, timeout=0):
    print('select({}, {}, {}, {}) ->'.format(readable, writable, exceptional, timeout), end=' ')
    readable, writable, exceptional = select.select(readable, writable, exceptional, timeout)
    print('({}, {}, {})'.format(readable, writable, exceptional))

def main():
    inputs = [sys.stdin]
    outputs = [sys.stdout]
    excepts = inputs
    print('testing select() with no timeout')
    test(inputs, outputs, excepts)
    print('testing select() with timeout of 0.1 seconds')
    test(inputs, outputs, excepts, 0.1)
    print('testing select() with timeout of 5 seconds')
    test(inputs, outputs, excepts, 5)

if __name__ == '__main__':
    main()
