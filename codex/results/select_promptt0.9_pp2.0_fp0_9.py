import select
# Test select.select() behavior

# Does select() detect a closed write fd?
pipe_rd, pipe_wr = os.pipe()
for wfd in (-100, -1, 0, 256, pipe_wr):
    rfds, wfds, xfds = select.select([], [wfd], [])
    if (len(rfds) != 0 or len(wfds) != 1 or
        (xfds != [] and not is_resource_warning)):
        print("select([], [%d]) -> %r, %r, %r" % (wfd, rfds, wfds, xfds))

os.close(pipe_wr)
rfds, wfds, xfds = select.select([], [pipe_wr], [])
if len(wfds) != 1:
    print("select([], [%d]) -> %r, %r, %r (write end closed)" % (wfd, rfds, wfds, xfds))

# Does select() detect an unreadable fd?
for rfd in (-100,
