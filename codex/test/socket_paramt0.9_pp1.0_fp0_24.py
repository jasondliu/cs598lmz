import socket
socket.if_indextoname(10)

from netaddr import *

from budds import hosts
from budds.users import User
u = User("yo", "yo")
print(u.password)
u.set_password("yo")
print(u.password)
u.save()
User.get("yo")

from budds import hosts
from budds import networks
from budds.hosts import Host
from budds.hosts import Host
h = Host("1", mac="mac", hostname="hostnam")
h.save()


from budds import hosts
from budds.hosts import Host
from budds import networks
from budds import config

from budds import dhcp
dhcp.util.validate_mac("11:11:11:11:11:11")

hosts.MAC("11:11:11:11:11:11")

h = Host("19")
h.update()
h.active()  # Returns boolean
h.get_ip_assignment_object()

h.update(active=False, lease_end=datetime.now())


