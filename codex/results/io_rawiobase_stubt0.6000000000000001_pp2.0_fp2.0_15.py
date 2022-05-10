import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.file = open(filepath, 'rb')
        self.size = os.path.getsize(filepath)
    def read(self, size=-1):
        return self.file.read(size)
    def tell(self):
        return self.file.tell()
    def seek(self, offset, whence=io.SEEK_SET):
        self.file.seek(offset, whence)
    def close(self):
        return self.file.close()

def read_image_from_bytes(filepath):
    with open(filepath, 'rb') as f:
        image = Image.open(f)
        image = image.convert('RGB')
        return image

def read_image(filepath):
    image = Image.open(filepath)
    image = image.convert('RGB')
    return image

def save_image(image, filepath):
    image.save(filepath)

def resize_image(image, size):
    return image.resize(size
