import ctypes
import ctypes.util
import threading
import sqlite3

UI_SET_NATURAL_ORIENTATION=1
ENTRY_FRAME_COLOR=(200,200,200)
DISP_FRAME_COLOR=(200,200,200)

OPENCV_FOLDER=os.getcwd()
CV_LIB=os.path.join(OPENCV_FOLDER, "lib/libopencv.so")
HAAR_FILES=os.path.join(OPENCV_FOLDER, "lib/haarcascades/")

# cvLoadImage, cvSaveImage are in core.so, but I could not find core.so on the net. 
CV_CORE=os.path.join(OPENCV_FOLDER, "lib/libcvcore.so")
CV_HIGH=os.path.join(OPENCV_FOLDER, "lib/libcv.so")
CV_HIGH_FLANN=os.path.join(OPENCV_FOLDER, "lib/libcvaux.so")
