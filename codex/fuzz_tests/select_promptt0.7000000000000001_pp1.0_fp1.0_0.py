import select
# Test select.select()
# select.select() tests if we can read or write to a socket.
# select.select() takes three arguments:
#   (rlist, wlist, xlist)
# rlist = a list of sockets that you want to test to see if you can read from them
# wlist = a list of sockets that you want to test to see if you can write to them
# xlist = a list of sockets that you want to test to see if they will throw an error when reading or writing

# select.select() returns three lists:
#   (rlist, wlist, xlist)
# rlist = a list of sockets that you can read from
# wlist = a list of sockets that you can write to
# xlist = a list of sockets that will throw an error when reading or writing

# select.select() is blocking, meaning that it will wait until there is data
# to be read from a socket, or until it is possible to write to a socket.
# select.select() is also interruptable by signals, so it is perfect for
# monitoring multiple sockets for events.

# select.select() is a
