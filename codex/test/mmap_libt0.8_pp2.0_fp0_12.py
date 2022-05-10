import mmap
import sys
import time
import glob
import gzip


if len(sys.argv) < 3:
    print("Usage:", sys.argv[0], "DB_PATH ... OUT_DIR [FILTER_ID]")
    sys.exit(1)

DB_PATH = sys.argv[1]
OUT_DIR = sys.argv[-1]
FILTER_ID = sys.argv[-2]

if not os.path.exists(DB_PATH):
    print("Invalid DB_PATH:", DB_PATH)
    sys.exit(2)
