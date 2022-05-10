import mmap
import numpy as np

from blockBag import BlockBag
from blockBag import getDataBlockSize
import struct

class npyBag(BlockBag):
    def __init__(self, bagFilePath, dataPointsPerBlock=1000, numpyStruct=None, numpyStructChar=None):
        super().__init__(bagFilePath, dataPointsPerBlock=dataPointsPerBlock)
        self.numpyStruct = numpyStruct
        self.numpyStructChar = numpyStructChar
        self.f = None
    def openFile(self):
        self.f = open(self.bagFilePath,'rb')
    def closeFile(self):
        self.f.close()
    def getDataBlockSize(self):
        return getDataBlockSize(self.numpyStructChar)
    def getDataBlock(self,blockID):
        self.f.seek(blockID*self.getDataBlockSize(),0)
        data = self.f.read(self.getDataBlockSize())
        return np.array(struct.unpack(self.
