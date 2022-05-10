import mmap
# Test mmap.mmap()

filename = "/home/pi/.config/autostart.txt"
# Open file for reading
with open(filename, "r") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read content via standard file methods
    print(mm.readline())
    mm.seek(0) # Go to beginning of file
    print(mm.readline())

# Close the map
mm.close()
