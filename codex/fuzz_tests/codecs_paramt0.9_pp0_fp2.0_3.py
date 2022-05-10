import codecs
codecs.register_error('strict', codecs.ignore_errors)

class BrokenPipeError(Exception):
    pass

class S3FileLister(object):
    def __init__(self, bucket, prefix='', delimiter=None):
        self.bucket = bucket
        self.prefix = prefix
        self.delimiter = delimiter
        self._done_iterating = False

        if self.delimiter:
            self.fs = FileSystem(self.bucket, self.prefix, delimiter=self.delimiter)
        else:
            self.fs = FileSystem(self.bucket, self.prefix)

    def __iter__(self):
        return self

    def __next__(self):
        if not self._done_iterating:
            try:
                self.next()
                return self.obj
            except StopIteration:
                self._done_iterating = True
                raise StopIteration
        else:
            raise StopIteration

    def next(self):
        self.par_dir, self.obj = next(self.fs.glob
