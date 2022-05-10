import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


def main():
    libc = ctypes.CDLL(libname)
    libc.set_signal_handler.argtypes = [ctypes.c_int, FUNTYPE]
    libc.set_signal_handler.restype = ctypes.c_int
    func = FUNTYPE(signal_handler)
    libc.set_signal_handler(signum, func)
    print(f"signal handler for {signum} registered")
    print(f"sending signal {signum} to me")
    os.kill(os.getpid(), signum)
    print("exiting")


def signal_handler(_signum, _frame):
    print(f"Received signal {signum}")


if __name__ == "__main__":
    sys.exit(main())
