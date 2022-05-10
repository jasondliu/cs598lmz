import select
# Test select.select in a simple way
#
# There is no way to test that select.select is actually waiting for the
# requested I/O condition, since there is no way to do a select on part of a
# file descriptor set.
#
# Testing that it does return when the condition is satisfied is not so easy
# either.  Here are some approaches:
#
# * Use subprocesses:  This is generally a good idea, and is used below.
#   However, it is possible that the child process completes before select()
#   is called in the parent.  That is, the kernel might be so fast that the
#   pipe is filled before the parent calls select().  This can be worked around
#   (e.g. by having the child sleep for a moment before writing to the pipe),
#   but it is easier to use another approach.
#
# * Use threads:  This seems to be a common approach, but it has two problems:
#   (1) Thread-safety:  select() is not thread-safe, so unless the thread that
#   calls select() also does the I/O, access to the file descriptor
