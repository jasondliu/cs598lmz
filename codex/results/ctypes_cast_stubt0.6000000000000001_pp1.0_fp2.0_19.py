import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# numpy
import numpy as np
np.array(x)

# tensorflow
import tensorflow as tf
tf.convert_to_tensor(x)

# pytorch
import torch
torch.tensor(x)

# keras
from keras import backend as K
K.variable(x)

# mxnet
from mxnet import nd
nd.array(x)
```

### 1.3.3 安装

```
# 在python3.6+环境下安装，如果不指定版本，默认安装最新版本
pip install mxnet-cu92  # CUDA92
pip install mxnet-cu101  # CUDA101
pip install mxnet-cu102  # CUDA102

# 如果安装的是CUDA10.2
