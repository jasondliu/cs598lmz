import socket
socket.if_indextoname(1)

# The following code is used to create a random MAC address for the virtual machine
import random
import string

def randomMAC():
    mac = [ 0x52, 0x54, 0x00,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

# The following code is used to create a random IP address for the virtual machine
import random
import string

def randomIP():
    ip = [ random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255) ]
    return '.'.join(map(lambda x: "%d" % x, ip))

# The following code is used to create a random hostname for the virtual machine
import random
import string

