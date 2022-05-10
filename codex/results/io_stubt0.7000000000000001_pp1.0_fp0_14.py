import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--write", help="Write to a file")
parser.add_argument("--write-screenshot", help="Write to a file")
parser.add_argument("-s", "--save", help="Write to a file")
parser.add_argument("-l", "--load", help="Write to a file")
parser.add_argument("--load-screenshot", help="Write to a file")
parser.add_argument("-r", "--read", help="Write to a file")
parser.add_argument("--read-screenshot", help="Write to a file")
parser.add_argument("--load-save")
parser.add_argument("--load-save-screenshot")
parser.add_argument("--save-save")
parser.add_argument("--save-save-screenshot")
parser.add_argument("--save-load")
parser.add_argument("--save-load-screenshot")
parser.add_argument("--save-read")
parser.add_argument("
