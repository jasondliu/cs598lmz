import mmap

from org.slf4j import Logger, LoggerFactory
from ch.qos.logback.classic import LoggerContext

class MMapAppender(AppenderBase):
  def __init__(self):
    self.name = "mmap"
    self.filename = None
    self.maxsize = 1024 * 1024 * 1024 # 1GB
    self.mmap = None
    self.size = 0
    self.idx = 0
    self.setAppend(False)
    self.setContext(LoggerContext())
    self.logger = LoggerFactory.getLogger(self.__class__)

  def __drain(self, event):
    txt = self.layout.doLayout(event)
    self.size += len(txt)

    if self.size + len(txt) >= self.maxsize:
      self.logger.warn("File size reached maximum. Dropping message")
    else:
      self.mmap[self.idx:self.idx+len(txt)] = txt
      self.idx = self
