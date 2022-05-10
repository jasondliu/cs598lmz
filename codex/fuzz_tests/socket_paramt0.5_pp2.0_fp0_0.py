import socket
socket.if_indextoname(3)

# If your interface is not listed, you can use the following command to add it: 
# ifconfig en0 alias 10.0.0.1

# If you are using a full-featured version of Scapy, you can use the following command to list all available interfaces:
# print(ls())


# In[ ]:


# Use the following command to get the details of your interface:
get_if_hwaddr('en0')


# In[ ]:


# Use the following command to get the IP address associated with your interface:
get_if_addr('en0')


# In[ ]:


# Use the following command to get the MAC address associated with your interface:
get_if_hwaddr('en0')


# In[ ]:


# To get the list of all the available protocols, use the following command:
ls(IP)


# In[ ]:


# To get the list of all the available protocols, use the following command:
ls(TCP)


# In[ ]:


# To get the list of all the available protocols,
