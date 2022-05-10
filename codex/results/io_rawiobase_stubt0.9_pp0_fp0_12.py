import io
class File(io.RawIOBase):
    # File class to pass to cantera so it can try opening all files
    # The read and writemethods have been overriden so we can keep track of the files that are being opened
    # The read and write methods are overridden here. But writing and reading still does not occur.
    def __init__(self, name, mode='r'):
        self.name = name
        file_list.append(name)
        if mode == 'r':
            self.can_write = False
        else:
            self.can_write = True

        return super().__init__()

    def read(self, n=0):
        return b''

    def write(self, data):
        return


def file_finder(filename, mode='r'):
    return File(filename, mode=mode)

file_list = []
file_finder.file_list = file_list
file_finder.cti_path = None
file_finder.chemkin_path = None

# Short Function to Remove any parameters and values from a string
def get_parameters_and_values(
