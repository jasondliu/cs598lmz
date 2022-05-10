import mmap
import struct
import sys
import time

def main():
    print("Starting...")
    start_time = time.time()

    # Open the source file for reading
    try:
        source_file = open("/home/ubuntu/workspace/Python/input.txt", "rb")
    except IOError as e:
        print("Error opening file:", e)

    try:
        # Create a memory-map of the file, size 0 means whole file
        map_file = mmap.mmap(source_file.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
    except Exception as e:
        print("Error creating map:", e)
        map_file.close()
        source_file.close()
        sys.exit(1)

    # Get the size of the file
    map_size = map_file.size()

    # Format of the input file is:
    # <int32><int32>....
    # Read one number at a time
    # Convert from little-endian to native-endian

