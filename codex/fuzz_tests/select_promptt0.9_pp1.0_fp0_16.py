import select
# Test select.select
print('Running :')
rlist, wlist, xlist = select.select([sys.stdin], [], [], 5)
if rlist:
    print('Input available')
else:
    print('Timed out')


# Timing out on network I/O
# 传统的方法，网络超时测试：

# Problem:
# Some forms of I/O can block for substantial periods of time.
# For instance, making a network connection or waiting for some
# form of user input can cause a program to block for a long time.

# Solution:
# There is no single solution for implementing timeouts on blocking
# I/O operations.
# On servers, it might make sense to implement some form of timeout
# on accept() calls to prevent a system from getting overloaded
# by requests.
# For processes that use a GUI, it probably makes sense to install
# callback functions that will get called periodically.
# For long-running computations, it might make sense to implement
# some form of watchdog timer that will
