import select
# Test select.select function
print('Start select')

# Generate three sockets for IO multiplexing.
# Sockets would be used for rlist and canbe used for wlist and xlist.
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Generate three pipes for IO multiplexing.
# Pipes is opened in O_NONBLOCK mode,
# and set read and write fd's to non-blocking mode.
rfd, wfd = os.pipe()
pr = os.fdopen(rfd, 'wb', 0)
pw = os.fdopen(wfd, 'rb', 0)
prfd, pwfd = os.pipe()
prr = os.fdopen(prfd, 'rb', 0)
pww = os.fdopen(pwfd, 'wb', 0)

