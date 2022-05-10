import socket
socket.if_indextoname("4")

# ## Initialization

# In[ ]:


if os.name == 'nt':
    separator = '\\'
else:
    separator = '/'

# ## Wifi auto disabling

# In[ ]:


code = """

import os
import time
import psutil

cpu_usage = psutil.cpu_percent()

while True:
    if psutil.cpu_percent(interval=None) > 50:
        os.system("netsh interface set interface 'Wi-Fi' admin=disabled")
        break
        
    time.sleep(1)
    
"""


# In[ ]:


with open("temp.py", "w") as file:
    file.write(code)


# In[ ]:


os.system("python temp.py")


# ## Checking for update

# In[ ]:


# Update check
if os.path.isdir('UpdateCheck'):
    os.system('rd /s /q UpdateCheck')


# In[ ]:


os.mkdir("
