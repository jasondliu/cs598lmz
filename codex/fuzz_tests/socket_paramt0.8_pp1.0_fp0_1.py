import socket
socket.if_indextoname('3')

print('\n=============================\n')

import subprocess
print(subprocess.check_output('ipconfig'))
