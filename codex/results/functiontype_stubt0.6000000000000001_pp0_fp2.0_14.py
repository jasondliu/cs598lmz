from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))


# In[8]:


# yield from
def gen():
    yield 1
    yield 2
    yield 3
def gensub():
    yield from gen()
    yield from 'abc'
for x in gensub():
    print(x)


# In[9]:


# 生成器迭代器
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(10):
    print(i)


# In[10]:


# 生成器
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(10):
    print(i)


# In[11]:


# 生成器
def my_range(n):
    i = 0
    while i < n:
