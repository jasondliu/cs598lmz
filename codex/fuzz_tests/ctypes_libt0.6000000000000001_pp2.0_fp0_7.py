import ctypes
ctypes.CDLL("libcaffe.so", mode=ctypes.RTLD_GLOBAL)
import caffe


def get_net(model_path, model_name, deploy_path, deploy_name, device_id=0):
    caffe.set_mode_gpu()
    caffe.set_device(device_id)
    net = caffe.Net(deploy_path + deploy_name, model_path + model_name, caffe.TEST)
    return net


def get_net_cpu(model_path, model_name, deploy_path, deploy_name):
    caffe.set_mode_cpu()
    net = caffe.Net(deploy_path + deploy_name, model_path + model_name, caffe.TEST)
    return net


def extract_feature(net, image, layer='fc7'):
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', np.array([104,
