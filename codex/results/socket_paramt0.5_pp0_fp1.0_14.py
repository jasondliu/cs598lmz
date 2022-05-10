import socket
socket.if_indextoname(1)

# In[ ]:


def get_mask(s):
    import struct
    import socket
    mask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << 32 >> int(s))))
    return mask


# In[ ]:


def get_ip_range(ip, mask):
    import struct
    import socket
    ip_int = struct.unpack('!I', socket.inet_aton(ip))[0]
    mask_int = struct.unpack('!I', socket.inet_aton(mask))[0]
    start = socket.inet_ntoa(struct.pack('!I', ip_int & mask_int))
    end = socket.inet_ntoa(struct.pack('!I', ip_int | ~mask_int))
    return start, end


# In[ ]:


def get_ip_range_from_cidr(cidr):
    ip, mask = cidr.split('/')
    start, end = get_ip_range(ip, get
