import select
# Test select.select
def test_select():
    """ Simple test for select.select """
    import select
    import socket
    if not hasattr(socket, 'AF_UNIX'):
        return
    s1 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s1.bind(support.TESTFN)
    s1.listen(1)
    s2.connect(support.TESTFN)
    s, _, _ = select.select([s1], [], [], 0)
    s[0].close()
    s2.close()
# Test a bug in select.select where it skipped the first file descriptor
# when given a list.
def test_select_list_skipping():
    """ Test that select.select does not skip the first file descriptor """
    import select
    import socket
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
