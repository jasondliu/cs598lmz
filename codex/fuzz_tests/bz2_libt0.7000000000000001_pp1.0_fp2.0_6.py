import bz2
bz2.decompress(f_c).decode('utf-8')

from bz2file import BZ2File
with BZ2File(f_n, 'wb') as f:
    f.write(f_c)

with open(f_n, 'rb') as f:
    f_d = f.read()
f_d.decode('utf-8')

# 图片
import imageio
im = imageio.imread('../../resource/img/1.png')
imageio.imwrite('1.png', im)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2)
axes[0].imshow(im)
axes[1].imshow(im[::-1])
plt.show()

# 图片base64
from io import BytesIO
import base64
f = BytesIO()
imageio.imwrite(f, im, 'png')
data = base64.b64encode(f.getvalue()).
