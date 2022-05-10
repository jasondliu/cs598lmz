import select
# Test select.select

import sys, socket, select

host = socket.gethostname()
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

# connect to remote host
