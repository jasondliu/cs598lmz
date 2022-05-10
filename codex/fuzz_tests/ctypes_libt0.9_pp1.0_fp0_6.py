import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
ctypes.cdll.LoadLibrary('libmxnet.so')
'''

# 加载预先训练的Inception-v3模型，所谓的Inception-v3模型是指，Inception-v3网络块组成的网络在ImageNet数据集上训练所得的模型
# 假设训练好的Inception-v3模型的参数已保存在pretrained文件夹下的Inception-v3-0000.params文件，并以Inception-v3-symbol.json文件保存Inception-v3模型的计算图

