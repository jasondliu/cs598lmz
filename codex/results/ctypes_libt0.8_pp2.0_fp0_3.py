import ctypes
ctypes.cdll.LoadLibrary('libGxIAPI.so')
import CameraSDK.GxIAPI as GxIAPI

# ---------------------------------------------------------------------------------------------------------------------------------------
# 初始化相机，并设置采集连续图像
# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. 初始化相机
# 单目模式相机对象初始化
monocular_camera = GxIAPI.GxCamera()                        # 单目模式相机对象初始化
monocular_camera.init_device()                              # 初始化设备
monocular_camera.set_trigger_mode(GxIAPI.GX_TRIGGER_MODE_FREE_RUN)  # 设置触发模式为自由连续采集模
