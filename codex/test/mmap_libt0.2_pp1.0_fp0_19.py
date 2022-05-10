import mmap
import sys
import os

def get_file_size(file_path):
    """
    This function returns the file size
    """
    file_info = os.stat(file_path)
    return file_info.st_size

def main():
    """
    This is the main function
    """
    # Open the file
    fd = os.open("foo.txt", os.O_RDWR)

    # Memory map the file
    m = mmap.mmap(fd, 0)

    # Print the length of the memory map
    print("Memory map length:", len(m))

    # Print the file size
    print("File size:", get_file_size("foo.txt"))

    # Close the file
    os.close(fd)

