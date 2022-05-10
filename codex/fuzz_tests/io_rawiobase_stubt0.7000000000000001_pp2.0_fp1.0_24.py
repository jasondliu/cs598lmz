import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.length = os.path.getsize(file.name)

    def read(self, size=-1):
        if size==-1:
            size = self.length - self.file.tell()
        return self.file.read(size)

def get_args():
    parser = argparse.ArgumentParser(description='Parse some arguments.')
    parser.add_argument('-i', '--inputFile', default=None, required=True, help='Input file')
    parser.add_argument('-o', '--outputFile', default=None, required=False, help='Output file')
    parser.add_argument('-l', '--label', default=None, required=True, help='Label')
    parser.add_argument('-p', '--preprocess', default=None, required=True, help='Preprocessing method: imagenet or inception')
    return parser.parse_args()

def main():
    args = get_args()
    input_file = args.
