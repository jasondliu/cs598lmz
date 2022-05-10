import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File(object):
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = codecs.open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for filename in filenames:
    files.append(File(filename))

with ExitStack() as stack:
    files = [stack.enter_context(f) for f in files]
    for f in files:
        print(f.read())
</code>
This will open all the files, and if there are any errors, it will close them.

