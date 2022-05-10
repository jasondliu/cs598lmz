import ctypes
ctypes.cdll.LoadLibrary("libopencv_cudaimgproc.so")
ctypes.cdll.LoadLibrary("libopencv_cudawarping.so")

if __name__ == '__main__':
    img = imread('/home/nvidia/Downloads/test.png',0)
    img = cv.resize(img, (256, 256))
    img = cv.Canny(img, 200, 300)
    #img = cv.medianBlur(img, 5)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
