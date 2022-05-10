import mmap
import os

class MmapHandler:

    def __init__(self, cfg, logger):
        self.c = cfg
        self.log = logger
        self.map = None
        self.fd = 0
        self.__open()

    def __open(self):
        try:
            if self.map != None:
                self.__close()

            # self.log.info("Opening mmap with " + "rwxrwxrwx")
            self.fd = os.open(self.c.memory_file, os.O_RDWR | os.O_CREAT)
            self.map = mmap.mmap(self.fd, self.c.memory_size)

        except Exception as e:
            self.log.error('Failed to open mmap file: "' + self.c.memory_file + '" with error: ' + str(e))
            raise e

    def __close(self):
        if self.map != None:
            self.map.close()
            self.map = None

        if self.fd != 0
