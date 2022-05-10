import lzma
lzma.open(os.path.join('../input/train',"{0}.dat.xz".format(0)))

# In[ ]:


'''
BUILDING DATA PIPELINE
'''

# In[ ]:


# def load_data(path_to_data,path_to_train,path_to_test,**kwargs):
def load_data(path_to_train,path_to_test,**kwargs):
    
    # path_to_data=kwargs.get('path_to_data','../input')
    # path_to_train=kwargs.get('path_to_train','../input/train')
    # path_to_test=kwargs.get('path_to_test','../input/test')
    usecols=kwargs.get('usecols',None) #defaults to loading all columns, if needed please specify which columns to load
    filters=kwargs.get('filters','*')
    # Only provide columns to use if you really need to so that all other columns are used as well
   
