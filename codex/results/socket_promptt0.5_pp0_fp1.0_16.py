import socket
# Test socket.if_indextoname on non-existing interface

def test(cmd, input, expected):
    print('Input:    ', input)
    print('Expected: ', expected)
    print('Executing:', cmd)
    actual = eval(cmd)
    print('Actual:   ', actual)
    if actual != expected:
        print('FAILED')
    else:
        print('PASSED')

# Test socket.if_indextoname on non-existing interface
test('socket.if_indextoname(1)', '', 'Traceback (most recent call last):\n'
     '  File "<stdin>", line 1, in <module>\n'
     'OSError: [Errno 19] No such device')
