import threading
threading.currentThread().name

threading.current_thread().name

t = threading.current_thread()
t.getName()

t.setName("MyCustomThreadName")
t.getName()


# In[8]:


import threading

def my_function(my_number, my_iteration):
    for number in range(my_number):
        print(f"Iteration: {my_iteration}, number: {number}")

if __name__ == "__main__":
    thread1 = threading.Thread(name="thread1", 
                               target=my_function, 
                               args=(100, 1))

    thread2 = threading.Thread(name="thread2", 
                               target=my_function, 
                               args=(200, 2))

    thread1.start()
    thread2.start()


# In[9]:


import time
from datetime import datetime

