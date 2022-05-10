from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = None
del BZ2Decompressor.decompress

# check python version
if sys.version_info < (3,6):
    print("\n[!] Please use python version 3.6 or above!\n")
    exit()

# set wifi adapter
if len(sys.argv) >= 2:
    try:
        iface = sys.argv[1]
        subprocess.run(f'ifconfig {iface} up', shell=True)
    except:
        print("Invalid iface!\n")
        exit()

# memory allocation
handshakes = []
probes = []

# global variables
STORE_PATH = './outputs'
PWD_PATH = './words'
NO_CLIENTS = True
NO_HANDSHAKES = True
NO_PROBES = True

# colors
w = '\033[0m' #white (normal)
r = '\033[31m' # red
g = '\033[32m' # green
o = '\033[33
