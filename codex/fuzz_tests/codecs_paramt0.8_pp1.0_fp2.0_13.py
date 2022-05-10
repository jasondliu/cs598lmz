import codecs
codecs.register_error("replace_with_space",
                      lambda err: (u" ", err.start + 1))

def read_utf8(source):
    with codecs.open(source, 'r', 'utf8',
                     'replace_with_space') as f:
        return f.read()

def write_utf8(target, content):
    with codecs.open(target, 'w', 'utf8') as f:
        f.write(content)

def clean_line(line):
    return re.sub("(\s+|\d+|[^\w]+)", " ", line).strip()

def clean_text(text):
    return "".join(clean_line(line) for line in text.split("\n")
                   if len(line) > 0)

def clean_source(source):
    return clean_text(read_utf8(source))

def run_pipe(pipe, *args):
    return subprocess.Popen(pipe, stdout = subprocess.PIPE,
                            stdin = subprocess.PIPE,
