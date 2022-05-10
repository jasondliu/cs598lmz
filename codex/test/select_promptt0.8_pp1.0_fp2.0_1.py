import select
# Test select.select
#need to specify rlist or wlist or xlist
#Is the timeout specified in seconds i.e 100 = 100 seconds
#Can timeout be less than 1?
#What is the format of the return?
# Need to use select.epoll to listen for events
# select.poll
# select.select

#Need to create two sockets 1 for reading, 1 for writing
#1. Create two sockets, One for writing and one for reading
#2. select.epoll - Create event poller
#2.1 register write event on write sock
#2.2 register read event on read sock
#2.3 Epoll.poll - Wait for event to be ready
#2.4 On event, read/write
#3. Close sockets, epoll
#
#
#
#
#
#
#
#
#

#http://www.binarytides.com/python-socket-programming-tutorial/

# How to close a socket ?
#

#test create_socket
#test_create_listen_socket
#test_send_to_listen_socket
#test
