import socket
socket.if_indextoname(socket.if_nametoindex('en0'))
import struct
import fcntl

class Interface:
    def __init__(self):
        self.net_func = {}

    def __register_macros(self):
        for name in dir(fcntl):
            if name.endswith('_HOST'):
                host = getattr(fcntl, name)
                net = host & 0x0000ffff
                host = (host & 0xffff0000) >> 16
                self.net_func[host] = net

    def __len__(self):
        return len(self.net_func)

    def __str__(self):
        return str(self.net_func)

    def __add__(self, x):
        self.__register_macros()
        if type(x) == int:
            if self.net_func.get(x, ""):
                return self.net_func[x]
        else:
            print 'Wrong Input'
            raise ValueError

ty = Interface()
print ty+32
