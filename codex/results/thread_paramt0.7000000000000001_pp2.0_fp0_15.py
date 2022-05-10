import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hi'))


# In[ ]:


import threading 
threading.Thread(target=lambda: print('hi'))

# 파이썬은 이런식으로 함수가 되도록 동작할 수 있다. 이런 식으로 사용하는것을 익숙해질 필요가 있을듯.


# In[1]:


# 실습 3

import threading
threading.Thread(target=lambda: print('hi'))


# In[ ]:


# 실습 4

import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hi')).start()


# In[ ]:


#
