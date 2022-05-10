import mmap
# Test mmap.mmap() function

with open("/home/neko/Desktop/learning/python3/python3_programming/ch10_advanced_modules/file/writeable.txt", "r+") as f:
    # memory-map the file, size 0 means whole file
    f_map = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(f_map.readline())  # returns "" b""
    # read content via slice notation
    print(f_map[:5])  # returns b"Hello"
    print(f_map.size())
    # reset file pointer to the beginning before the mmap
    f.seek(0)
    kwargs = {"v": sys.version_info}
    print(f"{kwargs}")
    f.write("Version: {}.{}.{}\n".format(*sys.version_info))
    # update the map
    f_map.close()
