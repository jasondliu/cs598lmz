import socket
socket.if_indextoname(3)
</code>
But I want to find this network interface named <code>en0</code> which is needed sequentially to send UDP communication,  by using low level C code. 
How can I do that? What should I use? 


A:

This example uses the <code>ioctl</code> system call with the <code>getifaddrs</code> ioctl to loop through all the network interfaces retrieving their names. Although some network interface names may not be listed, e.g. <code>lo0</code>, however,  you should be able to find <code>en0</code> this way.
Run code:
<code># gcc -Wall find_network_interface.c -o find_network_interface &amp;&amp; ./find_network_interface
lo0: 1
gif0: 2
stf0: 3
en0: 4
p2p0: 5
en3: 6
bridge0: 7
awdl0: 8
en1: 9
</code>
Source code:
<code>#include &lt;stdio.h&gt;

