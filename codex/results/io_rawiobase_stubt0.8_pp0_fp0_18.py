import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.cur = 0
        self.open()

    def open(self):
        self.file = io.open(self.name, self.mode)

    def read(self, n=-1):
        if not self.file:
            self.open()
        res = self.file.read(n)
        self.cur += len(res)
        return res

    def tell(self):
        return self.cur

    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset)


class TorchDataset(Dataset):
    def __init__(self, batch_size=4, num_frames=16, data_path='', transform=None, do_preprocessing=False, normalize=None):
        super(TorchDataset, self).__init__()

        self.transform = transform
        self.data_path = data_path
        self.batch_size = batch_
