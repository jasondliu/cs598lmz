import mmap

from Config import Config
from Log import log
from Util import readFile, writeFile


class FileEncryptor:
  def __init__(self, config=Config(), blockSize=32 * 1024 * 1024, numThreads=1, nid=None):
    self.blockSize = blockSize  # Max encrypted block size
    self.numThreads = numThreads
    self.nid = nid
    self.config = config

  # Encrypt file with filesize=0 to generate secret
  def encrypt(self, srcFilepath, destFilepath, filesize):
    raise NotImplementedError()

  # Decrypt file with FileNum=0 to get secret
  def decrypt(self, srcFilepath, destFilepath, filesize):
    srcFile = open(srcFilepath, "rb")
    destFile = open(destFilepath, "wb")
    start = 0
    end = filesize
    orig = self.decryptRange(srcFile, destFile, start, end)
    srcFile.close()
    destFile.close()
    return orig


