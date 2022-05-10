import socket
from murmur import Murmur
import re

#class Murmur:
#        def __init__(self, host="127.0.0.1", port=64738, password=""):
#                self.server = Murmur.ServerPrx.checkedCast(Ice.stringToProxy("Meta:tcp -h 127.0.0.1 -p 6502"))
#        def info(self):
#                return self.server.getInfo()
#        def uptime (self):
#                return self.server.getUptime()
#        def sendmessage(self,text):
#                self.server.getState(100)
#                self.server.sendMessage(1,text)
#                self.server.getState(100)
def raise_flag(flag, x, y):
  flagcount=0
  cells=open('flag').readlines()
  for i in range(len(cells)):
    if flag in cells[i]:
      if (x,y) == (22,11):
        flagcount=1
