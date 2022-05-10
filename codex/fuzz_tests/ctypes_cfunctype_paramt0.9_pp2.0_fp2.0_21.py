import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
def f(x):
  return 2 * x
g = FUNTYPE(f)
g(10)


# ## 4.22 Windows ー バッチファイルを使う

# In[ ]:


import subprocess
subprocess.call('echo %PATH%')


# In[ ]:


subprocess.call('echo %MY_ENV%', shell=True)


# In[ ]:


subprocess.check_output('goto HELLO', shell=False)


# In[ ]:


subprocess.check_output('message HELLO', shell=True)


# In[ ]:


subprocess.call('dir *.py')


# In[ ]:


subprocess.Popen('dir *.py')


# In[ ]:


subprocess.Popen(['dir', '*.py'])


# In[ ]:


subprocess.Popen('dir *.py', stdout=subprocess.PIPE)


# In[ ]:
