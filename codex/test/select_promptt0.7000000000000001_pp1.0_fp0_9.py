import select
# Test select.select() with all possible combinations of the
# three arguments: r, w, x.
#
# The select() function in module 'select' can be used to wait
# until a file descriptor is ready for reading (= input available),
# writing (= ready to send output) or has an exceptional condition
# pending (= out-of-band data available on OOB channel).
#
# This test checks all of these conditions, and that the results
# are correct.
#
# The Python implementation of select() uses the BSD select()
# system call if it is available.  This call can indicate both
# "exceptional conditions" and "out-of-band data" with a single
# bit.  This means that the two cases cannot be distinguished.
# Therefore, this test only tests for "exceptional conditions",
# rather than for "out-of-band data" as well.
#
# This test uses pipes for the file descriptors.  It is not
# possible to send "out-of-band data" on pipes, so this test
# only really tests for "exceptional conditions" on pipes.
#
# This test was written
