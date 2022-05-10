import socket
socket.if_indextoname(5)

# In[ ]:


data = open('/tmp/server.log').read()
re.findall('\[.*\]', data)

# ### 8.Write a function to get the same result (8) but with key-value format
# 

# In[ ]:


def get_data(data):
    return dict(zip(re.findall('\[.*\]', data), 
                                 re.findall('\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]', data)))
d = get_data(data)
d


# ### 9.Write a function to get the same result (8) but with key-value format as dict where the key is the date and the value is a list of IP
# ```
# {'date': [ip, ip]}
# ```

# In[ ]:


def get_data_1(data):
    li_dt = re.findall('\[.*\]', data)
