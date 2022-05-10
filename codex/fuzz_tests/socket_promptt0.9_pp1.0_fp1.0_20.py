import socket
# Test socket.if_indextoname()

print 'Platform:', sys.platform
if sys.platform == 'win32':
    print 'skipped'
    sys.exit()

def test(indexstring, expected):
    index = string.atoi(indexstring)
    result = socket.if_indextoname(index)
    if result != expected:
        raise TestFailed('expected %r, got %r' % (expected, result))

for addr in (
    ('1', 'lo0'),
    ('2', 'lo0'),
    ('3', 'lo0'),
    ('4', 'lo0'),
    ('100', 'lo0'),
    ):
    test(*addr)

if sys.platform in ('linux2',):
    for addr in (
        ('1', 'lo'),
        ('2', 'lo'),
        ('3', 'lo'),
        ('4', 'lo'),
        ('100', 'lo'),
        ):
        test(*addr)

    # FreeBSD loopback
    # These are some random interfaces I found on my FreeBSD 4.8 box
    # (interface,
