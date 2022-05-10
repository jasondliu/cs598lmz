import socket
socket.if_indextoname(int(host[1]))

print(host)

# print(target_ip)
# print(target_udp)

# print('Кол-во пакетов для отправки:', sys.argv[3])

#sys.argv[3] = int(sys.argv[3])
#print(type(sys.argv[3]))


# for i in range(sys.argv[3]):
#     packet = IP(dst=target_ip, ttl=64)/UDP(dport=target_udp)
#     send(packet, inter=0.1, verbose=0)
#     print("Пакет", i+1, "отправлен")
