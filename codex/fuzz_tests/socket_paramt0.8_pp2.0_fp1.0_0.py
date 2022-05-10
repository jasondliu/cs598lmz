import socket
socket.if_indextoname(3)

# получение ip адреса интерфейса
network_interface = socket.if_indextoname(3)
interface_ip = netifaces.ifaddresses(network_interface)[netifaces.AF_INET][0]['addr']
print(interface_ip)

# получение всех ip адресов интерфейса
# import socket
# import netifaces
#
# # получение всех интерфейсов
# all_interfaces = netifaces.interfaces()
# print(all_interfaces)
#
# # получение индекса интерфейса
# index_of_interface = socket.if_nametoindex('
