import threading
# Test threading daemon.

# Suppose you want to start a new thread for a long but finite computation, such as downloading a file from Internet or reading a large file. If the program ends before your thread ends, the thread will die without doing anything. To avoid this, you should always set daemon to True when you create infinite loops in the thread.

# In[1]:


import threading, time


# In[3]:


def countdown(n):
    i = 0
    while i < n:
        i += 1
        time.sleep(1)
        print(i, '\n')


# In[10]:


t = threading.Thread(target=countdown, args=(10,))
t.setDaemon(True)
t.start()
t.join()


# In[ ]:
