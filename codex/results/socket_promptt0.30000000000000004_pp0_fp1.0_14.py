import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Test if_indextoname()
    # This test is only meaningful on UNIX systems with ifconfig installed.
    if os.name != 'posix':
        return
    if os.system('ifconfig -a >/dev/null 2>&1') != 0:
        return
    # Get all interfaces
    out = os.popen('ifconfig -a', 'r').read()
    ifs = re.findall('^([^ \t:]+):', out, re.MULTILINE)
    for ifname in ifs:
        try:
            idx = socket.if_nametoindex(ifname)
        except OSError:
            continue
        try:
            name = socket.if_indextoname(idx)
        except OSError:
            continue
        assert ifname == name, 'if_indextoname(if_nametoindex(%r)) == %r != %r' % (ifname, name, ifname)

try:
    socket
