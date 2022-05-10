import socket
# Test socket.if_indextoname(19)
ifname = socket.if_indextoname(19)
print(ifname)

# Test ethernet's Mac address
mac = EthAddr()
print(mac)
print(str(mac))
print(hex(mac))
print(int(mac))
print(mac == 0x080000000002)

# Test ipv4's Mac address
ip = IPAddr(0x0a2a0001)
print(ip)
print(str(ip))
print(hex(ip))
print(int(ip))
print(ip == 0x0a2a0001)

# Test ipv6's Mac address
ip6 = IPAddr6(0x080000000002)
print(ip6)
print(str(ip6))
print(hex(ip6))
print(int(ip6))
print(ip6 == 0x080000000002)

# Test path
path = Path()
path.Append(EthHere(0x080000000003), EthGoto(0x080000000002))
path.Append(IPv4Here(
