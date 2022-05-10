import select
# Test select.select()

# Create a pair of connected sockets

# Create a pair of connected sockets

def child():
    # Child reads from pipe
    pipe_out.close()
    while True:
        line = pipe_in.readline()[:-1]
        print('Child %d got [%s] at %s' % (os.getpid(), line, time.time()))

def parent():
    # Parent writes to pipe
    pipe_in.close()
    while True:
        for i in range(3):
            pipe_out.write(b'Spam %03d\n' % i)
            time.sleep(1)
        os.wait()
        print('Parent exiting')

pipe_in, pipe_out = os.pipe()

if os.fork() == 0:
    child()
else:
    parent()

# Create a pair of connected sockets

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket
