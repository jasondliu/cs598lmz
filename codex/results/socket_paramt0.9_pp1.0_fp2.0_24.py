import socket
socket.if_indextoname(2)
'eth1'
>>> socket.if_indextoname(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
socket.error: (95, '/lib/libc.so.6: invalid argument')
>>> socket.if_indextoname(100000000000000000000)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
socket.error: (19, 'No such device')
>>> socket.if_indextoname(0)
'lo'
>>> socket.if_indextoname(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
socket.error: (19, 'No such device')

    """

    def __init__(self):
        """ initialize """
        self.name_to_index = {}
        self.index_to_name = {}
        self.update()

    def update(self):
        """ Determine the device name and index for each known
            network interface.
        """

