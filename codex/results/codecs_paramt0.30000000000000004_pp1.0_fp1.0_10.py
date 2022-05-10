import codecs
codecs.register_error('strict', codecs.ignore_errors)

class S3BotoStorage(S3BotoStorage):
    def _open(self, name, mode='rb'):
        return codecs.open(self._get_local_path(name), mode, encoding='utf-8', errors='strict')

    def _save(self, name, content):
        # Get the proper name for the file, as it will actually be saved.
        if name is None:
            name = content.name

        name = self._clean_name(name)
        # Get the proper name for the file, as it will actually be saved.
        if name is None:
            name = content.name

        name = self._clean_name(name)
        # Save the file.
        return super(S3BotoStorage, self)._save(name, content)

class S3BotoStorageFile(S3BotoStorageFile):
    def __init__(self, name, mode, storage, buffer_size=1024*1024):
        self._storage = storage
        self._mode = mode
        self
