import socket
socket.if_indextoname(3)

ifconfig

ifconfig en0

ifconfig en0 | grep 'inet '

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2 | cut -d '.' -f4

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2 | cut -d '.' -f4 | cut -c1-3

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2 | cut -d '.' -f4 | cut -c1-3 | tr -d '\n'

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2 | cut -d '.' -f4 | cut -c1-3 | tr -d '\n'

ifconfig en0 | grep 'inet ' | cut -d ' ' -f2 | cut -d '.' -f4 | cut -c1-3 | tr -d '\n' | tr -d '\n'

ifconfig en0 |
