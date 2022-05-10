import socket
socket.if_indextoname('3')

# The following should be equivalent to the above
import netifaces
netifaces.if_name(3)

# The following should print the MAC address of the interface
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

# The following should print the IPv4 address
netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
</code>
I am trying to get a list of all the interfaces in the machine and then get the MAC address, IPv4 address and IPv6 address of each interface.
I have tried to do that with the following code:
<code>import netifaces as ni

for interface in ni.interfaces():
    print interface
    print '\t' + ni.ifaddresses(interface)[ni.AF_LINK][0]['addr']
    print '\t' + ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
</code>
This works fine, but when I add the following line:
<
