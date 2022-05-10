import select
# Test select.select()
import socket

# sockets == channels to send/recv data between programs
# wait until the socket is ready to be read/written (or timeout)

# Data sources with select():
#   sockets(servers/clients)
#   devices(files, pipes)
#   stdin/stdout/stderr

# select.select(read_list,write_list,exception_list,timeout)

# select(): wait for events
# poll(): check for events
# epoll(): more flexibility for kernel events
# kqueue(): BSD/Apple

# select:
#   - handles everything (file descriptors, sockets, devices)
#   - limited to 2048 file descriptors on Linux
#   - cross-platform (Windows, Linux, Mac)
#   - simple syntax

# poll:
#   - handles everything (file descriptors, sockets, devices)
#   - no FD limit
#   - cross-platform
#   - more advanced syntax

# epoll:
#   - handles everything (file descriptors, sockets, devices)
#   - handles large number of file descript
