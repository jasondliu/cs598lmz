import select
# Test select.select
#
# For example, to read from stdin and all sockets.
# This works also for pipes and other file descriptors
# that support the select interface.

socks = [sys.stdin, sock1, sock2]

while True:
    inready, outready, exready = select.select(socks, [], []) # Wait forever until anything happens.
    for s in inready:
        if s == sys.stdin:
            sys.stdout.write("from stdin: " + sys.stdin.readline())
        elif s == sock1:
            sys.stdout.write("from sock1: " + sock1.recv(1024).decode("utf-8"))
        elif s == sock2:
            sys.stdout.write("from sock2: " + sock2.recv(1024).decode("utf-8"))
