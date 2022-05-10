import socket
socket.if_indextoname(3)

#获取网卡状态
#返回一个元组，元组内容为网卡状态
#SIOCGIFFLAGS：获取网卡状态
#SIOCSIFFLAGS：设置网卡状态
#SIOCGIFADDR：获取网卡IP地址
#SIOCSIFADDR：设置网卡IP地址
#SIOCGIFDSTADDR：获取网卡广播地址
#SIOCSIFDSTADDR：设置网卡广播地址
#SIOCGIFBRDADDR：获取网
