import select
# Test select.select
def test_select():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('google.com', 80))
    print 'Connected to google.com'
    s.send('GET / HTTP/1.1\r\n')
    while True:
        rlist, _, _ = select.select([s], [], [])
        if rlist:
            data = rlist[0].recv(100)
            print data
            break
    s.close()

# Local Variables:
# flycheck-flake8-maximum-line-length: 120
# End:
