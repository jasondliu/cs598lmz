import socket
socket.if_indextoname(2)
</code>
should return maybe <code>'en0'</code> or <code>'en1'</code> instead of <code>'lo0'</code>.

I am aware that the solution would be to use <code>socket.gethostbyname_ex(socket.gethostname())[2][1]</code> and then to get the second value of the second list which contains all the IPs of the computer. But I would like to know if I'm missing anything...

The code works fine on my Linux OS and on different Mac OS machines (10.8 and 10.9), but does not work on the one I need it to work on.
Thanks for your help,
Charly


A:

<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.gethostbyname_ex(socket.gethostname())
('DARWIN-LAPTOP.local', ['DARWIN-LAPTOP.local'], ['192.168.1.100'])
&gt;&gt;&gt; for ip in socket
