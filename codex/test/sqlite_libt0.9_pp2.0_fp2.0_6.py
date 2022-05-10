import ctypes
import ctypes.util
import threading
import sqlite3
 
# class CameraMeasureError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
 
class Camera(object):
    def __init__(self, index=0):
        self.index = index
        self.getCamerInfor()

    def getCamerInfor(self):
        self.name = threading.Thread(target=self.getName)
        self.name.start()
        self.sn = threading.Thread(target=self.getSn)
        self.sn.start()
        self.ip = threading.Thread(target=self.getIp)
        self.ip.start()
        self.link = threading.Thread(target=self.getLink)
        self.link.start()
        return [self.sn,self.ip,self.link]

    def getName(self):
        self.name = api.Ddp_GetCameraName(self.index)
        return self.name


