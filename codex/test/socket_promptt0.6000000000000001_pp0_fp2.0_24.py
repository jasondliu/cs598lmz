import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    # Create a temp file
    fd, fname = tempfile.mkstemp()

    # Write the file
    fp = os.fdopen(fd, 'w')
    fp.write("""
    1 lo
    2 eth0
    3 eth1
    4 lo
    """)
    fp.close()

    # Change /proc/net/dev
    old = "/proc/net/dev"
    os.rename("/proc/net/dev", fname)
    os.symlink(fname, "/proc/net/dev")

    # Test socket.if_indextoname()
    assert socket.if_indextoname(1) == 'lo'
    assert socket.if_indextoname(2) == 'eth0'
    assert socket.if_indextoname(3) == 'eth1'
    assert socket.if_indextoname(4) == 'lo'

    # Cleanup
    os.unlink("/proc/net/dev")
