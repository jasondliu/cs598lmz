import select
# Test select.select()
# This function is used to monitor multiple file descriptors, waiting until one or more of
# the file descriptors become "ready" for some class of I/O operation (e.g., input possible).
# The first three arguments are sequences of file descriptors to be waited on:
# rlist: wait until ready for reading, wlist: wait until ready for writing and xlist: wait for an "exceptional condition"

# The optional 4th argument specifies a timeout in seconds (see documentation in the python standard library)
# a tuple of three lists is returned: [rlist, wlist, xlist].
# the subselect function lets you specify a time interval in which the select function will time out
# If the time interval is missed, the function times out and returns None, []
# Command to run in shell:
# $ echo "socket" | nc -l 1234
# You should see the output "Hello socket" and then the program returns to the prompt
