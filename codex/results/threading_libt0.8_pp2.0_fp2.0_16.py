import threading
threading.activeCount()

def th1():
    print("TH1")
    time.sleep(2)
    print("TH2")
def th2():
    print("TH3")
    time.sleep(4)
    print("TH4")


# In[13]:


t1= threading.Thread(target=th1, args=())
t2= threading.Thread(target=th2, args=())
t1.start()
t2.start()

# In[ ]:
