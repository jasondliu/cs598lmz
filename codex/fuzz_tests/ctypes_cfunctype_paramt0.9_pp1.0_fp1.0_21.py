import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, HANDLE, ULONG, POINTER(ULONG))


def _loop(fn):
    while (1):
        n_bytes = ULONG(0)
        rc = fn(HANDLE(0), 0, n_bytes)
        n_bytes = n_bytes.value
        if n_bytes == 0:
            break
        yield n_bytes


def _quest():
    SetConsoleTitleA.restype = BOOL
    rc = SetConsoleTitleA("Is the game running?")
    assert rc
    print("Please wait...")


@FUNTYPE
def _show(h, n, lenptr):
    sys.stdout.write("\r")
    sys.stdout.write("%d bytes" % (n,))
    sys.stdout.flush()
    return 0


@FUNTYPE
def _file_show(h, n, lenptr):
    sys.stdout.write("%d\n" % (n,))
    return 0


@FUNTYPE
def _file_write(h, n,
