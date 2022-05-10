import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, wait up to that number of seconds and then return
#
# Return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready

# file descriptor:
# 0: stdin
# 1: stdout
# 2: stderr

# Usage:
# 	python select_test.py
#	> please input something:
#	> aaa
#	> you input: aaa
#	> please input something:
#	> bbb
#	> you input: bbb
#	> please input something:
#	> ccc
#	> you input
