import ctypes
ctypes.cast(0, ctypes.py_object).value


# In[13]:


#import win32clipboard
#win32clipboard.OpenClipboard()
#win32clipboard.GetClipboardData()
#win32clipboard.CloseClipboard()


# In[14]:


import subprocess
def run(cmd):
    subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)


# In[15]:


run('C:\\Program Files\\Mozilla Firefox\\firefox.exe')


# ### 【問題2】これまで利用してきたライブラリについて簡単に調査
# パッケージの中には便利なサブモジュールや関数がたくさんあります。これまで見つけてきたものは
# 
# - re

