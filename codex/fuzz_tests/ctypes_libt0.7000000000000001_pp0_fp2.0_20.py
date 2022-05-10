import ctypes
ctypes.cdll.LoadLibrary("../Release/bin/libNetwork.so")
import libNetwork

libNetwork.initialize(0)
libNetwork.loadStruct("../data/test.txt")
libNetwork.loadEmb("../data/test.emb")
libNetwork.loadLabelVec("../data/test.label")
data_x = libNetwork.getX()
data_y = libNetwork.getY()
print(data_x[0])
print(data_y[0])
libNetwork.release()
