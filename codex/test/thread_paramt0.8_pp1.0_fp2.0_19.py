import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r>> I will be printed last')).start()
print('\r>> I will be printed first')
sleep(1)
print('\r>> I will be printed second')
sleep(1)


# In[ ]:


# Python program to illustrate 
# Converting simple list to dictionary 
  
# Function to convert  
def Convert(list): 
    return tuple(list) 
      
# driver code 
list = [1, 2, 3, 4] 
print(Convert(list))
