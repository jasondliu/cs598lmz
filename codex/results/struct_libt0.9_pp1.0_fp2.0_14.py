import _struct
import _time

#==============================================================================
    
_kHandler = None
    
class _SMBTimeoutException(Exception):
    pass

class _SMBNoHandlerException(Exception):
    pass

class _SMBHandler(object):
    def __init__(self):
        self.sessionID = 0
        self.treeID = 0
    
    def SMBWrite(self, packet):
        length = _struct.pack('<h',len(packet))
        cmd = _struct.pack('BB',0xFF,0x53)
        req = length + cmd + packet
        res = _os.write(self.getfd(), req)
        if res != 0:
            raise _SMBTimeoutException
        res = _os.read(self.getfd(), 4)
        if res[-1] != 0:
            raise _SMBNoHandlerException
        return res
    
    def SMBRead(self):
        cmd = _struct.pack('BB',0xFF,0x53)
        req = cmd
        res = _os.write
