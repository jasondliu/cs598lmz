import lzma
lzma.LZMA_AVAILABLE = False

import cbz
import cbr
import rarfile
import zipfile

try:
    import rarfile
    rarfile.RarFileError
except (ImportError, AttributeError):
    rarfile = None

try:
    import libarchive
    libarchive.ArchiveError
except (ImportError, AttributeError):
    libarchive = None

if rarfile and rarfile.UNRAR_TOOL:
    rarfile.UNRAR_TOOL = "unrar-nonfree"
    rarfile.UNRAR_TOOL = "unrar"

if rarfile:
    def is_rarfile(filename):
        if not os.path.isfile(filename):
            return False
        with rarfile.RarFile(filename, 'r') as rar:
            return rar.needs_password()

    def get_rarfile_file(filename):
        with rarfile.RarFile(filename, 'r') as rar:
            return
