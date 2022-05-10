import select
# Test select.select()

# Register the socket to monitoring
# Registering the socket to the select() function, we just add the socket to the list, the second parameter
# is an empty list, we add to the first list, then we monitor the read list and exception list

# Use select.select()
# The first parameter is a list, containing all the monitored objects
# The second parameter is a list, containing the monitored objects when they can be read
# The third parameter is a list, containing the monitored objects when they can be written
# The fourth parameter is a list, containing the monitored objects when they have exceptions
# The fifth parameter is the timeout interval

# select.select(rlist, wlist, xlist[, timeout])
# If the timeout is negative, the function will block until the event is triggered
# If the timeout is zero, the function will not block
# If the timeout is positive, the function will block for a maximum of timeout seconds

# select.kepoll()
# select.kepoll() is an enhanced version of select.select(), which is the same as select.select()
# The parameter is the same as the parameter of select.select()
