import threading
threading.stack_size(67108864) 


def plt_show(mode='notebook'):
    if mode == 'notebook':
        get_ipython().run_line_magic('matplotlib', 'inline')
    elif mode == 'inline':
        get_ipython().run_line_magic('matplotlib', 'inline')
    elif mode =='qt5':
        get_ipython().run_line_magic('matplotlib', 'qt5')
    elif mode =='tk':
        get_ipython().run_line_magic('matplotlib', 'tk')



# In[3]:


def get_buffer(path):
    with open(path,'rb') as f:
        return f.read()
    


# In[42]:


def show_compare(img1,img2,size=(15,15)):
    f,axs = plt.subplots(2,1,figsize=size)
    axs[0].imshow(mpimg.imread(img1))
    axs
