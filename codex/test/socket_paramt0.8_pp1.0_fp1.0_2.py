import socket
socket.if_indextoname("en0")


# In[4]:


from scapy.all import *
pkts = rdpcap("http.pcap")
pkts[0]


# In[5]:


[pkt for pkt in pkts if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0]


# In[6]:


from scapy.all import *
pkts = rdpcap("http.pcap")
[pkt for pkt in pkts if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0]


# In[7]:


from scapy.all import *
pkts = rdpcap("http.pcap")
[pkt for pkt in pkts if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 1]


# In[8]:


from scapy.all import *
pkts = rdpcap("http.pcap")
