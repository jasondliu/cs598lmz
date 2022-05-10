import socket
socket.if_indextoname("23")

# ctypes_interface.h
def iplen():
        buf = c_buffer(OFP_MAX_PORT_NAME_LEN)
        lib.if_indextoname(23, buf)
        return buf.value

print("%s" % iplen())
</code>
output:
<code>Interface '23' doesn't exist
&lt;class 'bytes'&gt;()
</code>
Can anyone help me understand the above problem?
Thanks


A:

The first argument of <code>if_indextoname()</code> must be the network interface index (integer), not the network interface name (string) as you have in your code.
The network interface index is a parameter representing the network interface configuration. You can obtain the network interface index by using <code>if_nametoindex()</code> function. The <code>if_nametoindex()</code> function returns the network interface index of the interface named ifname or 0 if the interface does not exist.

