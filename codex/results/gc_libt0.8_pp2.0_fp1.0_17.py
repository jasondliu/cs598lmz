import gc, weakref
import os

class Row(list):
    def __init__(self, *args, **kwargs):
        self.data = kwargs.get('data', None)
        self.idx = kwargs.get('idx', None)
        self.name = kwargs.get('name', None)
        self.parameters = kwargs.get('parameters', dict())
        self.tags = kwargs.get('tags', list())
        self.run = kwargs.get('run', None)
        self.img = kwargs.get('img', None)
        self.parent = None
        if self.img is not None:
            assert isinstance(self.img, Image)
        super().__init__(*args)

    def __getitem__(self, y):
        if isinstance(y, str):
            assert self.data is not None, 'Cannot use row keys if there is no data.'
            return self.data[y][self.idx]
        else:
            return super(Row, self).__getitem
