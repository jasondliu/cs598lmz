from types import FunctionType
list(FunctionType(lambda a,b: a+b, globals(), "add", (a,b), 0))

# In[ ]:


# 使用自定义函数
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("The result is %s." % result)
        return result
    return wrapper

@print_result
def add(a, b):
    return a + b

add(1, 2)

# In[ ]:


# 使用lambda函数
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("The result is %s." % result)
        return result
    return wrapper

add = print_result(lambda a, b: a + b)
add(1, 2)

# In[ ]:


# 使用lambda函数
def print_result(func):
    def wrapper(*args
