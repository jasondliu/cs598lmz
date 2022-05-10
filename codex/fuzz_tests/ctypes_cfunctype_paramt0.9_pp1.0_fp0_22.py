import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_int)

def readGDB(command, *args):
	"""Call a GDB command"""
	arguments = " --args ".join(["gdb", command] + list(args))
	return os.popen(arguments).read()

def parseLines(input):
	input = input.splitlines()
	indices = [i for i, line in enumerate(input) if "expand" in line]
	indices = [0] + indices + [len(input)]
	return [input[indices[i]+1:indices[i+1]]
			  for i in range(len(indices)-1)]


def parseAtoms(input, prefix_common=lambda e,i: e):
	"""Parse a list of atoms from input

	A numeric is a token that is either a single number, or enclosed in single or double quotes

	A list of atoms looks like::
	   0: (void *) 0x0
	   1: (void *) 0x7fff5fbffc
