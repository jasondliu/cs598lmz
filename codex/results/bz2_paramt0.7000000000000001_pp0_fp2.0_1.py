from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

import numpy as np
import matplotlib.pyplot as plt

# Make a plot of sin(x) and cos(x) between -pi and pi
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x), '-k', label='sin(x)')
plt.plot(x, np.cos(x), '--r', label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x), '-k', label='sin(x)')
plt.plot(x, np.cos(x), '--r', label='cos(x)')
pl
