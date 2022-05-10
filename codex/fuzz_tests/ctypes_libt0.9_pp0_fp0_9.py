import ctypes
ctypes.windll.shell32.IsUserAnAdmin()


# In[2]:


if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print("Not admin")
else:
    print("Admin")


# In[8]:


import ctypes
import logging
import win32api, win32con
import os


# In[9]:


import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def run_as_admin(argv=None, debug=False):
    python_exe = sys.executable

    if argv is None:
        argv = sys.argv
    if hasattr(sys, 'frozen'):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        arguments = map(unicode, argv[1:])
    else:

