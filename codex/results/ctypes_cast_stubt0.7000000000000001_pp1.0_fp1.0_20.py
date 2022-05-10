import ctypes
ctypes.cast(addr, ctypes.py_object).value


# ## <font color='red'>Exercise</font>  
# - Using `ctypes` on the `shm_addr` above, convert the buffer at this address into a numpy array. 
# - Print the resulting array, and compare it to the array we created above.

# In[7]:

# Use ctypes to convert the shm_addr buffer into a numpy array

import ctypes
# YOUR CODE HERE
shm_array = ctypes.cast(shm_addr, ctypes.py_object).value
shm_array


# ## <font color='red'>Exercise</font>  
# - What happens if you change the `shm_array` in the previous step? Does the original array that we created above change as well? Why or why not? 
# - What about the other way around? What happens if you change the original array? Does the `shm_array` change? Why or why not? 

# In[8]:

# Try changing the shared memory array, and see if the other one changes.


