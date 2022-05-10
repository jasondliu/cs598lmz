import socket
socket.if_indextoname(2)

# In[ ]:


#finding the endianness of the system
import sys
if sys.byteorder == "little":
    print("Little Endian")
else:
    print("Big Endian")

# In[13]:


#Printing the Information on current CPU and Memory usage using psutil
import psutil
print("CPU Usage Per Process % ", psutil.cpu_percent())
print("RAM Usage: % ", psutil.virtual_memory())

# In[14]:


#Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
