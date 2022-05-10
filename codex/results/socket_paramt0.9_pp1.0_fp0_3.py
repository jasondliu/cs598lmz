import socket
socket.if_indextoname(socket.if_nametoindex("eth1"))
</code>
then it is giving me output as
<code>'eth1'</code>
and finally closing my ssh connection


A:

You have to have the same python interpreter on the same Linux machine.
Please note that you have to have the exact same <code>os.uname()</code> tuple:
<code>os.uname()
</code>
if running on the "local" machine and the same one on the "remote"
machine.
Quite often the SSH tunnel is used to make the "remote" machine appear
to be the "local" from the viewpoint of the "remote"
process:
<code>ssh -L local_port:remote_ip:remote_port user@remote_host
</code>
In such a way the "remote" interpreter will see exactly the same
interface names and the same number
<code>os.uname()
</code>

