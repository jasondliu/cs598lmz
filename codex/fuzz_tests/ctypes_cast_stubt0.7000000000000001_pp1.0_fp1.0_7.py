import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = '/home/guotai/Documents/Project/Python/PIL/lena.jpg'
img = cv2.imread(img_path)

# %%
# convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# %%
# set color threshold
lower_blue = np.array([0, 0, 100])
upper_blue = np.array([100, 100, 255])

# %%
# find the colors within the specified boundaries and apply the mask
mask = cv2.inRange(img, lower_blue, upper_blue)
output = cv2.bitwise_and(img, img, mask=mask)

# %%
# show image
plt.imshow(output)

# %%
