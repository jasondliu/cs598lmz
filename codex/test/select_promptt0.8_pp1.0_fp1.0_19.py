import select
# Test select.select
# Input data
fd_num = 100
timeout = 1
# Create a list of file descriptors
fd_list = []

for i in range(0, fd_num):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 0))
    sock.listen(128)
    fd_list.append(sock.fileno())

# Start timer
start = time.time()

while True:
    rlist, wlist, xlist = select.select(fd_list, fd_list, fd_list, timeout)
    end = time.time()
    # Go out of this loop when timeout exceeded
    if end - start > timeout:
        break

# Clean up
for sock in fd_list:
    os.close(sock)

