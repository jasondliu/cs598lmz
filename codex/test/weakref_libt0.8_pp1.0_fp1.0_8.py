import weakref

from ase.io import write,read
from ase.calculators.calculator import Calculator


class PLDFile(file):
    def __init__(self, filename, mode='r'):
        file.__init__(self, filename, mode=mode)
        self.n = -1

    def readline(self):
        self.n += 1
        return file.readline(self)

    def __del__(self):
        self.close()

