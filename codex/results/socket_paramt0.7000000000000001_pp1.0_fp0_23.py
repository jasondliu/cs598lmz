import socket
socket.if_indextoname("1")

# In[ ]:


import psutil
psutil.cpu_percent(interval=1)
psutil.cpu_percent(interval=1, percpu=True)

# In[ ]:


import os
os.getcwd()
os.chdir("C:\\")
os.getcwd()

# In[ ]:


import socket
socket.gethostname()

# In[ ]:


import multiprocessing
multiprocessing.cpu_count()

# In[ ]:


import shlex, subprocess
command_line = "dir"
args = shlex.split(command_line)
print(args)
subprocess.call(args)

# In[ ]:


import platform
platform.system()
platform.release()

# In[ ]:


import os
os.getlogin()

# In[ ]:


import psutil
psutil.cpu_count()

# In[ ]:


import multiprocessing
multiprocessing.cpu_count()

