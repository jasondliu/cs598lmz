import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\Users\hong\Desktop\바탕화면\2.jpg" , 0)

# 화면을 어둡게 한다.
ctypes.windll.user32.SetDeviceGammaRamp(0, ctypes.c_void_p(0))

# 화면을 밝게 한다.
ctypes.windll.user32.SetDeviceGammaRamp(0, ctypes.c_void_p(1))

# 화면 밝기를 낮춘다.
ctypes.windll.user32.SetDeviceGammaRamp(0, ctypes.c_void_p(2))

# 화면 밝기를 높인다.
ctypes.windll.user32.SetDeviceGammaR
