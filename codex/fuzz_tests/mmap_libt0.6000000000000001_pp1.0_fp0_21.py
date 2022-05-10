import mmap
import numpy
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image

shape = (720, 1280)
image = numpy.zeros(shape, dtype=numpy.uint8)

for i in range(shape[0]):
    for j in range(shape[1]):
        image[i,j] = i*j%256

print image.shape

plt.imshow(image, cmap = cm.Greys_r)
plt.show()

im = Image.fromarray(image)
im.save("test.bmp")
