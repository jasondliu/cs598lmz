import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def close(self):
        logging.info("close")

    def read(self, length=None):
        logging.info(f"read({length})")
        return b"A"

    def write(self, b):
        logging.info(f"write({b})")
        return len(b)

with open('spam.log', 'w') as f:
    logging.basicConfig(filename='spam.log', level=logging.DEBUG)
    file = File("foo.txt", "r")
    text = file.read()
    file.write(text)
    file.close()
