import mmap
# Test mmap.mmap(0, 1, "Molecule", mmap.ACCESS_READ)

# Test if the file is a molecule file

def isMoleculeFile(filename):
    """ Test if a given file is a molecule file """
    try:
        # Test header
        with open(filename, "rb") as f:
            header = f.read(4)
            if header != "MOLE":
                return False
            return True
    except:
        return False

# Test if the file is a molecule file

def isMoleculeFile(filename):
    """ Test if a given file is a molecule file """
    try:
        # Test header
        with open(filename, "rb") as f:
            header = f.read(4)
            if header != "MOLE":
                return False
            return True
    except:
        return False

# Test if the file is a molecule file

def isMoleculeFile(filename):
    """ Test if a given file is a molecule file """
    try:
        # Test header
        with open(filename, "rb
