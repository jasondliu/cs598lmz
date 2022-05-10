import socket
socket.if_indextoname(1)
</code>
I get this error:
<code>OSError: [Errno 19] No such device
</code>
I am running this on a virtual machine, so perhaps that is the problem?


A:

By default, Scapy uses the first interface as the default interface. In your case, this is loopback, which is probably not what you want.
You can use the following to get all interfaces:
<code>&gt;&gt;&gt; [x[0] for x in scapy.utils.ifaces()]
['lo', 'eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'eth5', 'eth6', 'eth7', 'eth8', 'eth9', 'eth10', 'eth11', 'eth12', 'eth13', 'eth14', 'eth15', 'eth16', 'eth17', 'eth18', 'eth19', 'eth20', 'eth21', 'eth22', 'eth23', 'eth24', 'eth25', 'eth26', 'eth27', 'eth28', 'eth29', 'eth30',
