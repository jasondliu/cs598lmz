import codecs
codecs.register_error("strict", codecs.ignore_errors)

def read_file(filename, encoding="utf-8"):
    with codecs.open(filename, encoding=encoding) as f:
        return f.read()


def write_file(filename, data, encoding="utf-8"):
    with codecs.open(filename, "w", encoding=encoding) as f:
        return f.write(data)


def read_dir(directory, encoding="utf-8"):
    for filename in os.listdir(directory):
        if os.path.isdir(filename):
            continue
        yield os.path.join(directory, filename), read_file(filename, encoding=encoding)


def read_files(files, encoding="utf-8"):
    for filename in files:
        yield filename, read_file(filename, encoding=encoding)


def read_files_with_suffix(files_or_dir, suffix, encoding="utf-8"):
    if os.path.isdir(files_or_dir):
        for filename in os.
