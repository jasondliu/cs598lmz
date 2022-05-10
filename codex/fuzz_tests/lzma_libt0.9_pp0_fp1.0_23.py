import lzma
lzma.LZMA.NONE = lzma.CHECK_NONE
lzma.LZMA.CRC32 = lzma.CHECK_CRC32
lzma.LZMA.SHA1 = 13

# ------------------------------------------------------------------------------

def d0_files(path):
    for path in list_files(path):
        if os.path.splitext(path)[1] == ".d0":
            yield path


def _run_bg(argv, stdin_input=None, cwd=None, ignore_errors=False):
    logger.info("running %r", str(argv))
    startupinfo = None if os.name == 'nt' else subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    subprocess_flags = 0
    try:
        subprocess_flags = subprocess.CREATE_NEW_PROCESS_GROUP
    except AttributeError:
        pass
    try:
       
