import mmap
class RReader():
    def __init__(self, file_path, chunk_size = 2**20, find_new_files = True):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.find_new_files = find_new_files
        self.get_file_location()

    def get_file_location(self):
        if self.find_new_files:
            filenames = [f for f in os.listdir(self.file_path)]
            filenames = [f for f in filenames if f[0] != '.']
            if len(filenames) == 0:
                print("No files in directory", file_path)
                return
            filenames = sorted(filenames, key = lambda x: os.stat(os.path.join(self.file_path, filenames[0])).st_size)
            latest_file = filenames[-1]
            print("latest file: ", latest_file)
            file_loc = self.file
