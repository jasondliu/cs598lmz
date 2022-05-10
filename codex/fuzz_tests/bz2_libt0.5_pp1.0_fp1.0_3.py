import bz2
bz2.decompress(bz2_data)

#图像读取
import base64
import imghdr
from PIL import Image
import io

def base64_to_image(b64_data):
    b64_data = b64_data.replace('data:image/jpeg;base64','')
    b64_data = b64_data.replace('data:image/png;base64','')
    b64_data = b64_data.replace('data:image/gif;base64','')
    b64_data = b64_data.replace('data:image/jpg;base64','')
    b64_data = b64_data.replace('data:image/bmp;base64','')
    b64_data = b64_data.replace('data:image/jpeg;base64','')
    b64_data = b64_data.replace('data:image/jpeg;base64','')
    b64_data = b64_data.replace('data:image/jpeg
