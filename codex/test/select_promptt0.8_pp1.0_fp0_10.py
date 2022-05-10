import select
# Test select.select function
#
# Get two pipes and put one end in each rlist
# and the other in wlist.
#
# Write a character to the writable pipe.
#
# Select should return the readable pipe.
rlist, wlist, xlist = select.select([], [], [])

pp1, pp2 = os.pipe()

rlist, wlist, xlist = select.select([pp1], [pp2], [])

# XXX This code is broken: if writing to pp1 or reading from pp2
#     would block, this test would hang.  This is fixed in
#     pybsddb/test/test_select.py, which uses pipes that can be
#     written to and read from without blocking (see, e.g.,
#     test_not_enough_fds).  But the FreeBSD test_select module
#     still uses the same pipes, so it hangs too.  If we fix that
#     test, this test should be fixed (or replaced) too.
