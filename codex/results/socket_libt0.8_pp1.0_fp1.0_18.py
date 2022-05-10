import socketio
from tensorflow.keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import numpy as np

sio = socketio.Client()
speed_limit = 10


def img_preprocess(img):
    img = img[60:135, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img


@sio.on('telemetry')
def 
