import codecs
codecs.register_error("strict", codecs.ignore_errors)

def f_open(filename, mode):
    return codecs.open(filename, mode, 'utf-8')

def read_file(filename):
    with f_open(filename, "r") as f:
        return f.read()

def write_file(filename, data):
    with f_open(filename, "w") as f:
        return f.write(data)

def read_file_lines(filename):
    lines = read_file(filename).splitlines()
    lines = [line.rstrip("\r\n") for line in lines]
    while lines and not lines[-1]:
        del lines[-1]
    return lines

def write_file_lines(filename, lines):
    with f_open(filename, "w") as f:
        f.write("\n".join(lines))
        f.write("\n")

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


