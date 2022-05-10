import socket
import struct

# 默认的请求头
HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'
}

# 默认的超时时间(s)
TIMEOUT = 60

# 内网网卡地址
IF_NAME = 'enp6s0'

# 组播组地址
GROUP_IP = '224.0.0.142'


def get_addr(ip, if_name=IF_NAME):
    """
    获取本机内网网卡IP
    :return: str
    """
    return socket.gethostbyname_ex
