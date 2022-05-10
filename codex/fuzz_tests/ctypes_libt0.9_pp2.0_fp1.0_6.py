import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


# 设定图像的大小

# In[2]:


fig=plt.figure()
fig.set_size_inches(11,6)


# 导入图像

# In[3]:


image=mpimg.imread('julyimage.png')


# 显示图像

# In[4]:


img=plt.imshow(image)


# 设计图标标题

# In[5]:


font={'family':'Arial Unicode MS'}
plt.rc('font',**font)
plt.title('2014年7月份阿甘州天气温度走势图')


# 修改横坐标值

# In[6]:


x=np.linspace(0
