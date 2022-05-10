from types import FunctionType
list(FunctionType(f.__code__,
                  f.__globals__,
                  f.__name__,
                  f.__defaults__,
                  f.__closure__) for f in df.columns)

# ## 6.7 Dictionary modifications

# ### Modifying using `dict.update`

# In[6]:


url_template = 'http://places.kmz'

def generate_url(**kwargs):
    return url_template.format_map(kwargs)

generate_url()


# In[7]:


class GenerateUrl:
    def __init__(self, url_template=None, **kwargs):
        self._template = url_template or "http://places.{state}.{domain}"
        self.url_kwargs = kwargs
        
    def update_templace(self, **kwargs):
        copy = self.url_kwargs.copy()
        copy.update(kwargs)
        return copy
    
    def __call__(self, **kwargs):
        update = self.update_tem
