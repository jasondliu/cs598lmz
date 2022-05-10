import socket
socket.if_indextoname(1)

# In[ ]:


get_ipython().system_raw('./ngrok http 9000 &')


# In[ ]:


url=! curl -s http://localhost:4040/api/tunnels | python3 -c \
    "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
url=url[0].replace('https://','').replace('http://','')
print(url)


# In[ ]:


get_ipython().system_raw('python3 app.py &')


# In[ ]:


from flask import Flask, render_template,request
from werkzeug import secure_filename
from gevent.pywsgi import WSGIServer
from flask_ngrok import run_with_ngrok
from keras.models import load_model
from keras.preprocessing import image
from fastai.vision import *
import numpy as np
import cv2
import os
from PIL import Image
from resizeimage import resize
