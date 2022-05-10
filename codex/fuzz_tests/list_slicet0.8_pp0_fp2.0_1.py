import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])#点击函数


# In[10]:


# 冒泡排序
lst = [9,9,1,1,2,2,3,3,4,4,5]
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)


# In[11]:


a=None
a=a or 'default'
print(a)


# In[12]:


lst=[1,2,3,4,5]
lst[1]=lst
print(lst)


# In[13]:


def a(b):
    return b+1
print(a(3))


# In[14]:


def a(b,c=1,*d,**e):
    print(b,c)

