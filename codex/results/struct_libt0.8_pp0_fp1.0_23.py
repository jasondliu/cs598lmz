import _struct

class Checksum(object):
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return _struct.crc16(_struct.pack('<I', self.data))

def wrap(data):
    return _struct.pack('>H',len(data)) + data

class Command:
    Noop = 0x01
    ReadMemory = 0x02
    WriteMemory = 0x03
    ReadRegisters = 0x04
    WriteRegisters = 0x05
    ReadEEPROM = 0x06
    WriteEEPROM = 0x07
    ReadPeripherals = 0x08
    WritePeripherals = 0x09
    Reset = 0x0a
    Echo = 0x0b
    Execute = 0x0c
    ReadVersion = 0x0d
    ExecuteNew = 0x0e
    ReadPeripheralsEx = 0x0f
    WritePeripheralsEx = 0x10
    WriteRegistersEx = 0x11
    ReadMemoryEx = 0x12
   
