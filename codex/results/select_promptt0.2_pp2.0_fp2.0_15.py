import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are lists of file descriptors to be waited for
#   reading, writing, or error conditions, respectively.
# timeout is an optional float specifying a timeout in seconds.
#   If timeout is omitted the select blocks until at least one file
#   descriptor is ready.
# A 3-tuple of lists is returned, containing those descriptors that are
#   ready for reading, writing, and error conditions, respectively.

# select.poll()
# select.poll() is a cross-platform alternative to select.select()
#   that works on Unix and Windows.
# It supports the same operations as select.select()
#   but it returns a list of (fd, event) 2-tuples,
#   one for each descriptor that has an event or error condition to report.
# The event field is an integer containing event flags.
#   The flags are the same as those returned by select.select()
#   and can be tested using the constants defined in the select module.
# The event field can be tested
