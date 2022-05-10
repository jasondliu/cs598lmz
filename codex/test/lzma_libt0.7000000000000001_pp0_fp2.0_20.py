import lzma
lzma.open

def save(text, file_name):
    '''Save an object as a compressed pickle file.
    '''
    file = gzip.GzipFile(file_name, 'wb')
    file.write(text)
    file.close()

def load(file_name):
    '''Loads a compressed pickle file.
    '''
    file = gzip.GzipFile(file_name, 'rb')
    buffer = ""
    while True:
        data = file.read()
        if data == "":
            break
        buffer += data
    file.close()
    return buffer

def load_data(file_name):
    '''Loads a compressed pickle file.
    '''
    file = lzma.open(file_name, 'rb')
    buffer = ""
    while True:
        data = file.read()
        if data == "":
            break
        buffer += data
    file.close()
    return buffer
