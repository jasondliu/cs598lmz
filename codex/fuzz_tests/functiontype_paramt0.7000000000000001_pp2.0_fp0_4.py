from types import FunctionType
list(FunctionType('f', globals(), 'return 1').__code__.co_names)

# In[ ]:
