import ctypes
ctypes.cdll.LoadLibrary("caffe2_nvrtc.dll")
import caffe2.python.onnx.backend as backend

g_tf_path = "D:\\NAV_TF\\"
g_caffe2_path = "D:\\NAV_Caffe2\\"

def get_npy_path():
    return g_tf_path + "npy/"

def get_ckpt_path():
    return g_tf_path + "ckpt/"

def get_log_path():
    return g_tf_path + "log/"

def get_predict_path():
    return g_tf_path + "predict/"

def get_model_path():
    return g_tf_path + "model/"

def get_data_path():
    return g_tf_path + "data/"

def get_test_data_path():
    return g_tf_path + "test_data/"

def get_caffe2_model_path():
    return g_caffe2_path + "model/"

