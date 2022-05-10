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

class PLD(Calculator):
    """Class for doing Precision Local Descriptors calculations.

    Parameters:

    atoms: Atoms object
        The atoms to be relaxed.
    pld_file: str
        Name of the PLD file.  This file contains the position of the atoms and
        the PLD descriptor.  It is written by the PLD code.
    write_pld_file: bool
        If true the PLD file is written.  The default is false.
    command: str
        Command for executing PLD.  It should be something like:
        '/home/matsc
