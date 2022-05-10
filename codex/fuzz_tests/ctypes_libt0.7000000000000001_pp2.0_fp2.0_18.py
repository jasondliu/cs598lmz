import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import cv2 as cv

# 找到视频中最亮的像素点的坐标

cap = cv.VideoCapture(0)

while True:
    # 读取视频中的每一帧
    _, frame = cap.read()
    # 转换成灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 找到灰度图中最大的像素点的位置
    maxVal = gray.max()
    minVal = gray.min()
    print(minVal, " ", maxVal)
    min_loc = cv.minMaxLoc(gray)
    print(min_loc)
    # 找到灰度图中最大的
