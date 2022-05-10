import socket
socket.if_indextoname(1)

# Get_ipaddress_by_interface_name(‘ens9’)
import socket
socket.if_indextoname(1)
socket.if_nameindex()[2]

# resolv.conf
import socket
import struct
import fcntl


class Network:

    """
    This class represents the resolv.conf file.
    """

    def __init__(self, conf_file='/etc/resolv.conf'):
        self.servers = []
        self.domain = ''
        self.search = []
        self.sortlist = []
        self.options = []

        fp = open(conf_file, 'r')
        for line in fp:
            line = line.rstrip('\n')
            if line == '' or line.lstrip().startswith(';'):
                continue

            fields = line.split()
            if len(fields) < 2:
                raise Exception('Invalid line in /etc/resolv.conf: %r' % line)

            keyword = fields
