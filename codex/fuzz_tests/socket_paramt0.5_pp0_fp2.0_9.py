import socket
socket.if_indextoname(1)

import subprocess

p = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
output, err = p.communicate()
print output
</code>

