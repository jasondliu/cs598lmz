import ctypes
ctypes.cdll.LoadLibrary('/media/w_programs/Develop/OpenCV/opencv-3.4.5/build/lib/libopencv_videoio.so')
ctypes.cdll.LoadLibrary('/media/w_programs/Develop/OpenCV/opencv-3.4.5/build/lib/libopencv_imgproc.so')
ctypes.cdll.LoadLibrary('/media/w_programs/Develop/OpenCV/opencv-3.4.5/build/lib/libopencv_imgcodecs.so')
ctypes.cdll.LoadLibrary('/media/w_programs/Develop/OpenCV/opencv-3.4.5/build/lib/libopencv_core.so')
import cv2


def get_screenshot(filename='screenshot.png', device=0):
    cap = cv2.VideoCapture(device)
    ret, img = cap.read()
    if not ret:
        print("Got ", ret)
        raise Exception("Can't get image from device")
    cv2
