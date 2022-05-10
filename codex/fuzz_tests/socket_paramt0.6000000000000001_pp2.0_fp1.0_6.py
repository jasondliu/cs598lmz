import socket
socket.if_indextoname(1)

# In[ ]:


def get_connection_info(interface):
    if_name = socket.if_indextoname(interface)
    if_addrs = netifaces.ifaddresses(if_name)
    if netifaces.AF_INET in if_addrs:
        for addr in if_addrs[netifaces.AF_INET]:
            if addr['addr'] == '127.0.0.1':
                continue
            return {
                'dst_ip': addr['addr'],
                'dst_mac': if_addrs[netifaces.AF_LINK][0]['addr'],
                'src_ip': socket.gethostbyname(socket.gethostname()),
                'src_mac': if_addrs[netifaces.AF_LINK][0]['addr']
            }
    return {}

def get_dst_info(dst_ip):
    dst_ip = dst_ip.strip()
    if dst_ip in ['127.0.0.1', '
