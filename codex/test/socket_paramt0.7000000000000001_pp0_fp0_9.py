import socket
socket.if_indextoname(3)

exit(0)

import netifaces
import struct as st

# 本地ip地址
# localIP = netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']
localIP = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# 子网掩码
# localMask = netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['netmask']
localMask = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['netmask']

# 网关
# localGate = netifaces.gateways()['default'][netifaces.AF_INET][0]
localGate = netifaces.gateways()['default'][netifaces.AF_INET][0]

# 转换为整数
localInt = st.unpack
