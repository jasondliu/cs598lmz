import mmap
import os

from . import utils


class File(object):
    def __init__(self, file_path, name=None):
        self.path = file_path
        self.name = name or os.path.basename(file_path)


class FileManager(object):
    def __init__(self, files, tmp_dir=None):
        self.files = files
        self.tmp_dir = tmp_dir or tempfile.mkdtemp()

    def __enter__(self):
        self.process_files()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clean_up()

    def process_files(self):
        for file in self.files:
            file.path = utils.normalize_file_path(file.path)

            if not os.path.exists(file.path):
                raise FileNotFoundError(f'File {file.path} not found')

            file.tmp_path = os.path.join(self.tmp_dir
