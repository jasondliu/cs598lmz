import io
class File(io.RawIOBase):
    def __init__(self, fh):
        self.fh = fh

    def writable(self):
        return True

    def write(self, b):
        # Ensure it's an UTF-8 byte string and write it
        return self.fh.write(str.encode(str(b), "UTF-8"))

f = File(sys.stdout)

print(f'{color.GREEN}The {color.UNDER_LINE}C++{color.END} way of creating objects that inherit from std::iostream{color.END}')

print(color.RED+'This does not print in the console'+color.END, file=f)
</code>
The output:

