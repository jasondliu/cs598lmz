import socket
socket.if_indextoname(1)

# ifconfig

# ipconfig /all

# ipconfig /allcompartments

# netsh interface show interface

# netsh interface ipv4 show address

# netsh interface ipv4 show address "Ethernet"

# netsh interface ipv4 show address "Ethernet" | find "IP Address"

# netsh interface ipv4 show address "Ethernet" | find "IP Address" | find ":"

# netsh interface ipv4 show address "Ethernet" | find "IP Address" | find ":" | findstr /v ":"

# netsh interface ipv4 show address "Ethernet" | find "IP Address" | find ":" | findstr /v ":" | findstr /v "IP Address"

# netsh interface ipv4 show address "Ethernet" | find "IP Address" | find ":" | findstr /v ":" | findstr /v "IP Address" | findstr /v "IPv4"

# netsh interface ipv4 show address "Ethernet" | find "IP Address
