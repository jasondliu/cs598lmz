import mmap
# Test mmap.mmap.read()

def main():
    fd = os.open("sample.bin", os.O_RDWR)
