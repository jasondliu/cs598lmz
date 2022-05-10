import mmap

def read_text_file(file_name):
  with open(file_name, "rb") as f:
    # mmap is used for memory mapping.
    # mmap is the modern and recommended way to read files
    # source:
    # https://stackoverflow.com/questions/17012708/fast-reading-from-large-file-in-python-without-memory-problems
    mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    text = mm.read(100).decode("utf-8")
    mm.close()
    return text

filename = input("Enter the file name: ")
print(read_text_file(filename))
