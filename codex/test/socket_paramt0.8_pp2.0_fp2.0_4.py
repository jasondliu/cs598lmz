import socket
socket.if_indextoname(12)

my_interface = input("Enter desired interface: ")
sniff(iface=my_interface, store=False, prn=process_sniffed_packet)
