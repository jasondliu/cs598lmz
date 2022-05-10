import socket
# Test socket.if_indextoname()
interface = 11
machine = socket.if_indextoname(interface)
LOG.debug("interface 11 name is %s." % machine)

exploit = "/usr/sbin/moxa_attach"
ip = "127.0.0.1"
port = 25
LOG.debug("Exploiting %s at IP %s." % (exploit, ip))

# To set socket option SO_BINDTODEVICE, we need to open a connection
# over the device and then issue .setsockopt() afterwards.
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((ip,port))
#s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, "\0%5s\0" % machine)
#LOG.debug("%d: %s" % (interface, s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE)))

# Create d-bus connection.
bus = dbus.SystemBus()
