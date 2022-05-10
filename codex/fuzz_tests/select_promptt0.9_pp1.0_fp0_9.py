import select
# Test select.select
# PIPE is a pipe on which we can select for read and write.
r,w = os.pipe()
# Selecting for read/write on a pipe that is not yet connected will
# cause an error.
try:
    print(select.select([r],[],[]));
except OSError as e:
    assert(e.errno == errno.ENOTCONN)
# Selecting for read/write on a pipe that has been closed will
# cause an error.
try:
    print(select.select([r],[],[]));
except OSError as e:
    assert(e.errno == errno.EBADF)


# Test os.read()
print(len(os.read(r, 10)))

# Test select.select
print(select.select([r],[],[]));

# Test os.write()
print(len(os.write(w, b"1234567890")))

# Test select.select
print(select.select([r],[],[]));

rlist,wlist,xlist = select.select
