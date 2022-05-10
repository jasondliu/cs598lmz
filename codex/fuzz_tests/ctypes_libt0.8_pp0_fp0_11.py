import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')
# 因为要推理，所以第一个参数是空，注意第二个参数是输入的形状，第三个参数是输出的形状
model = Caffe2Net(None, 'data', [(1,1,224,224)], ['softmax'] )

# 加载模型
model.load_model('resnet50/predict_net.pb', 'resnet50/init_net.pb')

# 初始化模型
workspace.RunNetOnce(model.init_net)

# 开始推理
workspace.FeedBlob('data', img)
workspace.RunNetOnce(model.predict_net)

# 获
