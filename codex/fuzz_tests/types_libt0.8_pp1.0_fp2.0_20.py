import types
types.NoneType


# In[99]:


def funcion(arg):
    arg()
    
    
    


# In[100]:


def otra_funcion():
    print("Hola")


# In[101]:


funcion(otra_funcion)


# In[102]:


import requests


# In[103]:


class Usuario:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        
        
    def __call__(self):
        return "{} {}".format(self.user, self.password)
    
    
        


# In[104]:


usu1 = Usuario("user","1234")


# In[105]:


usu1()


# In[ ]:
