import select
# Test select.select.
#
# The first argument should be a list of three lists of file descriptors.
# select replaces these with three lists of those file descriptors that are ready.
#
# The second argument is the list of file descriptors to be checked for write-readiness,
# and the third is the list to be checked for exceptions.
#
# Generally, timeouts are zero, so that select returns immediately,
# or negative, so that select blocks indefinitely.
#
# For example, suppose that fd1, fd2 and fd3 are open files.
# If r, w, e = select.select([fd1, fd2], [], [])
# then r will be a two-element list containing fd1 and fd2,
# since both are ready to be read.
#
# If r, w, e = select.select([fd1, fd2], [fd3], [])
# then r will be a two-element list containing fd1 and fd2,
# since both are ready to be read, w will be a one-element list containing fd3,
# since it
