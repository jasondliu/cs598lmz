import select
# Test select.select
#    select_timeout

# Test select.error
#    errno
#    strerror

# Test select.poll
#    poll_test

# Test select.epoll
#    epoll_test

# Test select.kqueue
#    kqueue_test

# Test select.devpoll
#    devpoll_test


#----------
# Test select.select
#    select_timeout
# Now, we go get the select module, and call it with a timeout of 1 second
# and a dictionary of our read/write file descriptors.  We also time the
# call.  If the select.select function returns right away, we check to see
# if the timer has exceeded the timeout.  If not, we know that select is not
# working correctly, and we return an error.
#
# Otherwise, we return successfully.

from select import *
from time import time

def select_timeout(timeout):
    read_list = {0:0, 1:0}
    write_list = {0:0, 1:0}
