import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.path))).start()

import yaml
from pprint import pprint

from keras.models import model_from_yaml
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

def load_yaml_model(path):
    file = open(path, 'r')
    model_str = file.read()
    file.close()
    model = model_from_yaml(model_str)
    return model

def load_img_to_array(path):
    img = load_img(path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_class(model, img_arr):
    predictions = model.predict(img_arr)
    class_index = np.argmax(predictions[0])
   
