import socket
port = 12345
print port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', port))
s.recv(1024)
</code>
And the output looks like:
<code>Traceback (most recent call last):
  File "client.py", line 7, in &lt;module&gt;
    s.recv(1024)
socket.error: [Errno 10054] An existing connection was forcibly closed by the remote host

I have tried changing ports, but that doesn't seem to change anything.
</code>
Update: It seems like this won't work for me, I guess. I don't know what happened to it.
After I restarted my computer, the connection through the code appears to work.
If you are using Eclipse, make sure you aren't running the server and client at the same time. You may have to restart eclipse to do this. Also make sure that any firewall that you have isn't blocking the communication.

