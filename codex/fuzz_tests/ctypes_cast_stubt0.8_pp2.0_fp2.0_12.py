import ctypes
ctypes.cast(0, ctypes.py_object).value

# Read our input file.
import sys
(filepath, output_file) = sys.argv[1:]
with open(filepath, "rb") as fil:
    data = fil.read()

# Write our output file.
with open(output_file, "wb") as fil:
    # Write the header.
    fil.write("#!./target/debug/instr.bytecode\n")
    # Write the data length.
    fil.write(struct.pack("<I", len(data)))
    # Write 
