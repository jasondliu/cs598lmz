from lzma import LZMADecompressor
LZMADecompressor().decompress(file_content)

################################################################################
# methods for encoding, decoding and copying
################################################################################
def encode_data(data):
    '''
    Encode the data using base64
    
    Parameters
    ----------
    data: bytearray
        The data that should be encoded

    Returns
    -------
    data: bytes
        The encoded data
    '''
    data = base64.b64encode(data)
    return data

def decode_data(data):
    '''
    Decode the data using base64
    
    Parameters
    ----------
    data: bytes
        The data that should be decoded

    Returns
    -------
    data: bytes
        The decoded data
    '''
    data = base64.b64decode(data)
    return data

def copy_file(src_path, dest_path):
    '''
    Copies a file from one location to another. This method is used to copy the 
    file from the bucket to a local directory. If a file is copied, the copied
    file
