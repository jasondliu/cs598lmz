import io
class File(io.RawIOBase):
    ...

def ReadableFileName(FileName):
    File = open(FileName, 'rb')
    return File

def ReadableDir(FileName):
    File = open(FileName, 'rb')
    return File, FileName

def WriteableFileName(FileName):
    File = open(FileName, 'wb')
    return File, FileName

def OpenFileName(FileName):
    File = open(FileName, 'rb')
    return File, FileName

def IsReadWrite(File):
    return File.readable() and File.writable()

def IsReadWriteFileName(FileName):
    File = open(FileName, 'rb')
    return File.readable() and File.writable()

def HasChangelist(File):
    return File.changelist() != 0

def HasChangelistFileName(FileName):
    File = open(FileName, 'rb')
    return File.changelist() != 0

def DeleteFile(File, FileName):
    del File
    os.remove(File
