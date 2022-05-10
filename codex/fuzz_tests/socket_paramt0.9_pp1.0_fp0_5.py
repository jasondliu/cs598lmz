import socket
socket.if_indextoname(3)

# Можно перебрать все сетевые интерфейсы
for i in range(0, 100):              # Считаем, что интерфейсов не больше 100
    try:
        socket.if_indextoname(i)
    except:
        pass
    else:
        print(i, ':', socket.if_indextoname(i))

# Порты
for port in range(1, 1025):
    try:
        print(socket.getservbyport(port))
    except:
        pass

# Протоколы
protocols_full = {
    socket.IPPROTO_ICMP: 'icmp',  # 1
    socket.IPPROTO_IP: 'ip',  # 0
    socket.IPPROTO_
