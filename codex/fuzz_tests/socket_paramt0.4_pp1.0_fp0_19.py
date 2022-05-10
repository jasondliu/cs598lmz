import socket
socket.if_indextoname(1)

# In[ ]:


# 取得某个网络接口的IP地址
socket.gethostbyname('www.baidu.com')


# In[ ]:


# 取得某个网络接口的MAC地址
import uuid
uuid.getnode()


# In[ ]:


# 取得某个网络接口的MAC地址
import netifaces
netifaces.ifaddresses('en0')[netifaces.AF_LINK][0]['addr']


# In[ ]:


# 取得某个网络接口的MAC地址
import fcntl
import struct
def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGR
