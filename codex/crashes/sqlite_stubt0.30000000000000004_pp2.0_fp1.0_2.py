import ctypes.util
def main():
    lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
    lib.sqlite3_config(ctypes.c_int(4), ctypes.c_int(1))
if __name__ == '__main__':
    main()
