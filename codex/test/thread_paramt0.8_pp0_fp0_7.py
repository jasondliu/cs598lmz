import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n')).start()


# In[5]:


net_model, net_weights, net_classes, net_mean, net_scale, net_swap = (
    net_resnet50, 'ResNet-50-model.caffemodel', 'synset_words.txt',
    np.array([104., 117., 124.]), np.array([1]), (2,1,0)
)


# In[6]:


net = caffe.Net(net_model, net_weights, caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', net_mean)
transformer.set_transpose('data', net_swap)
transformer.set_raw_scale('data', net_scale)


# In[7]:


net.blobs['data'].reshape(1, *net.blobs['data'].data.shape[1:])


# ## Detecting Monty Python (MP
