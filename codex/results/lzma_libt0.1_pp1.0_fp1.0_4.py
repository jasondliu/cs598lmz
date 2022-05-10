import lzma
lzma.LZMAError:
    print("LZMAError")
    pass

try:
    import bz2
    bz2.BZ2Error:
        print("BZ2Error")
        pass
except:
    print("BZ2Error")
    pass

try:
    import zlib
    zlib.error:
        print("ZlibError")
        pass
except:
    print("ZlibError")
    pass

try:
    import gzip
    gzip.error:
        print("GzipError")
        pass
except:
    print("GzipError")
    pass

try:
    import zipfile
    zipfile.BadZipFile:
        print("BadZipFile")
        pass
except:
    print("BadZipFile")
    pass

try:
    import tarfile
    tarfile.TarError:
        print("TarError")
        pass
except:
    print("TarError")
    pass

try:
    import rarfile
    rarfile.RarCannotExec:

