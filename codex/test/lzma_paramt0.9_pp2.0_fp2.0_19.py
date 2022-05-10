from lzma import LZMADecompressor
LZMADecompressor_decompress = LZMADecompressor().decompress

############# ACCESSING METADATA ################

# Reads the structure metadata from IPC.ZIP (or a provided index file), returns that data
def get_structure_metadata(file):
    with zipfile.ZipFile(file) as IPCarchive:
        with IPCarchive.open("IPC2.txt") as index:
            return parse_index(index)

# Generate/parse an index file to a C++ source file, or use an existing one
def maybe_generate_index(file="IPC.zip", indexfile="IPC2.txt", output_format="cpp"):
    # A file exists with that name, assume it is valid
    if os.path.isfile("IPC2.txt"):
        return False
