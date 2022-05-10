import select
# Test select.select().

#         R  W  E
r, w, e = select.select([17], [17], [])
print('The returned empty lists are:', (r, w, e))

# If you pass it a list of file descriptors, like we did above,
# the call will return the subset of them that are ready for reading,
# for writing, and for an exception, respectively.

# If a file descriptor is in the returned list for 'reading',
# for example, that means that your program could call read() or recv()
# on it, and not get blocked. It does not necessarily
# mean that there is anything to read (it might mean the other endpoint
# has closed the connection).

# So, this program prints the empty lists.
# (It may occur to you to run this program,
# to get a better idea of what it does,
# but I think you can safely skip that. This is just a footnote.)


################################################################################
# Test select.poll().
#
#        R  W  E

p = select.poll()
# So we'll use select.
