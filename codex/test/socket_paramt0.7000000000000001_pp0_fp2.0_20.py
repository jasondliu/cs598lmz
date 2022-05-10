import socket
socket.if_indextoname(3)

# 在某些平台上可能需要root权限才能捕获数据包

# scapy被设计为不需要root权限即可查看和操作网络，
# 由于scapy是使用原始套接字来捕获数据，
# 所以Python必须以root身份运行，才能捕获数据包。
# 如果不是root用户，scapy只能使用AF_PACKET套接字，
# 这和tcpdump有点类似，
