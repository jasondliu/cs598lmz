import select
# Test select.select()

# Check to see if Select has been implemented.
try:
    select.select([], [], [], .1)
except AttributeError:
    print 'Select not implemented'
    sys.exit()

# Create a list of sockets.
socks = []
# Add a pipe to the list.
socks.append(os.pipe())
# Create a non-blocking socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
# Add the socket to the list.
socks.append(s)

# Wait until there is some data.
while True:
    (rlist, wlist, xlist) = select.select(socks, [], [], 1)
    if len(rlist) != 0:
        break
    print 'Waiting for data'

print 'Data is ready'
