import selectors
import socket
import sys
import threading

#hierarchical file structure
class ServerFileSystem(object):
    def __init__(self):
        self.files = {}
        self.files['/'] = File('/', is_dir=True, content='')

    def ls(self, path):
        assert path in self.files, 'Path {} does not exist'.format(path)
        file = self.files[path]
        assert file.is_dir, 'Path {} is not a directory'.format(path)
        return list(file.children)

    def mkdir(self, path):
        assert path not in self.files, 'Path {} already exists'.format(path)
        # add the directory to the parent directory
        parent_path = os.path.dirname(path)
        assert parent_path in self.files, 'Path {} does not exist'.format(parent_path)
        parent = self.files[parent_path]
        assert parent.is_dir, 'Path {} is not a directory'.format(parent_path)
        parent.children
