import io
class File(io.RawIOBase):
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self):
        print("exit")

    def __iter__(self):
        print("__iter__")
        return ("hello" , "beautiful" , "world")


if __name__ == '__main__':
    with File() as f:
        print(f)
        for line in f:
            print(line)
