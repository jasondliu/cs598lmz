import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


# In[ ]:


# Import all necessary libraries.
import cv2
import numpy as np
from keras.preprocessing import image
import pandas as pd 
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import matplotlib.pyplot as plt
import sys
import os
import time
from keras.models import load_model
import csv
import cv2
import numpy as np
from keras.preprocessing import image
import pandas as pd 
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import matplotlib.pyplot as plt
import sys
import os
import time
from keras.models import load_model
import csv
import gc


# In[ ]:


# Load the trained model
