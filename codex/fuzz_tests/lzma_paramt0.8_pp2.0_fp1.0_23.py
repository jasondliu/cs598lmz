from lzma import LZMADecompressor
LZMADecompressor().decompress(a)

a = lzma.decompress(a)
a

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()


ax = fig.add_subplot(111)

x = np.linspace(-1,3,100)
y = np.exp(-x**2)

ax.plot(x, y)
y2 = np.exp(-(x-0.5)**2/0.1**2)
ax.plot(x, y2, 'r--')
ax.fill(x,y2,'r')
ax.text(0,0.6, 'Gaussians')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25
