import select
# Test select.select
def test_select():
    conn_list = []
    read_list = []
    write_list = []
    error_list = []
    timeout = 10
    ret = select.select(read_list, write_list, error_list, timeout)
    print ret

# Test socket.socketpair
def test_socketpair():
    server_sock, client_sock = socket.socketpair()
    print server_sock.fileno()
    print client_sock.fileno()
    server_sock.close()
    client_sock.close()

# Test socket.SOCK_STREAM
def test_SOCK_STREAM():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    print sock.fileno()
    sock.close()

# Test socket.SOCK_DGRAM
def test_SOCK_DGRAM():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    print sock.fileno()

