import _struct
import random

# 协议的抽象类，定义协议的解码和编码方式及长度计算
class Protocol():
    def __init__(self, name = "", version="", encode='utf-8'):
        self.name = name
        self.version = version
        self.encode = encode

    def pack(self, name, value):
        raise NotImplementedError("Must implement the pack method!")

    def unpack(self, name, value):
        raise NotImplementedError("Must implement the unpack method!")

    def length(self, value):
        raise NotImplementedError("Must implement the length method!")

    def get_name(self):
        return self.name

    def get_version(self):
        return self.version

    def get_encode(self):
        return self.encode

class ProtocolText(Protocol):
    def
