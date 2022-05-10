import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# return value: three lists of objects that are ready

# select.poll()
# select.poll() is a cross-platform alternative to select()
# It supports registering multiple file descriptors to wait on
# It supports waiting for a specified timeout
# It supports waiting for events other than read readiness
# It supports waiting for multiple file descriptors at once
# It supports waiting for the same file descriptor as multiple different events
# It supports waiting for the same file descriptor as both a read and a write event
# It supports waiting for a file descriptor to become ready for reading or writing
# It supports waiting for a file descriptor to become ready for reading and writing
# It supports waiting for a file descriptor to become ready for reading or writing or for an exceptional condition
# It supports waiting
