import select
# Test select.select
# Use select function to create an I/O multiplexing
# Input is standard input, output is standard output,
# the other two is standard network port 80
import sys,time
inputs = [sys.stdin]
outputs = [sys.stdout]
exceptional = []

print '''
Select will return the tuple (inputs,outputs,exceptions)
which contains the subset of the corresponding file
objects that are ready: inputs will be the list of all
file objects that are readable; outputs will be the subset
of all file objects that are writable; exceptions will be
the subset of all file objects that has an exceptional
condition (an “exceptional condition” means an error that
is not a hangup or an interrupt); the returned list is
empty if the time limit is hit.

select.select(rlist, wlist, xlist[, timeout])

Given three lists of waitable objects (which may be
a mix of file descriptors, sockets, pipes, and kqueue
events), rlist are those to be waited on for readability,
wlist are those to be waited on for writ
