import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# 파이썬에서 윈도우 메시지 박스를 띄우는 방법은 여러가지가 있습니다.
# 그중 가장 간단한 방법은 ctypes 모듈을 사용하는 것입니다.
# ctypes 모듈은 파이썬에서 C 라이브러리를 사용할 수 있도록 해주는 모듈
