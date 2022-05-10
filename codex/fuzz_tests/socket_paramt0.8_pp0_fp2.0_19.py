import socket
socket.if_indextoname("4")

# try:
#     sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
#     sock.bind("lo")
# except socket.error, msg:
#     raise msg

# def get_if():
#     """
#     Get interface MAC of interface.
#     :return:
#     """
#     ifs = get_network_interfaces()
#     for i in ifs:
#         if i['name'] == args.ifname:
#             return i
#     return None
#
#
# def get_network_interfaces():
#     """
#     Get all host MAC addresses
#     :return:
#     """
#     is_64bits = sys.maxsize > 2 ** 32
#     struct_size = 40 if is_64bits else 32
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     max_possible = 8  # initial value
#     while True:
#        
