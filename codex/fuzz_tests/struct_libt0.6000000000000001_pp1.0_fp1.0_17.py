import _struct
import array

def read_bin(filename,dtype='f',count=-1):
    """
    Read binary file of floats
    """
    fid = open(filename,'rb')
    if count == -1:
        a = array.array(dtype)
        a.fromfile(fid,os.path.getsize(filename)/a.itemsize)
    else:
        a = array.array(dtype,fid.read(count))
    fid.close()
    return a

def read_bin_chunk(filename,dtype='f',count=-1,offset=0):
    """
    Read binary file of floats
    """
    fid = open(filename,'rb')
    if count == -1:
        fid.seek(offset,0)
        a = array.array(dtype)
        a.fromfile(fid,os.path.getsize(filename)/a.itemsize-offset)
    else:
        fid.seek(offset,0)
        a = array.array(dtype,fid.read(count))

