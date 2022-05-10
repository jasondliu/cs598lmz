import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(filename):
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_text_from_url(url):
    return get_text(urlopen(url))

def get_text_from_file(filename):
    return get_text(filename)

def get_text_from_stdin():
    return get_text(sys.stdin)

def get_text_from_string(string):
    return get_text(StringIO(string))

def get_text_from_bytes(bytes):
    return get_text(BytesIO(bytes))

def get_text_from_zip(zip_file, filename):
    with ZipFile(zip_file) as z:
        return get_text(z.open(filename))

def get_text_from_tar(tar_file, filename):
    with TarFile(tar_file) as t:
        return get_text(t.ext
