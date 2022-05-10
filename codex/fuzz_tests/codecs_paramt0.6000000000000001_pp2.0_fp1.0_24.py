import codecs
codecs.register_error('surrogate_pass', codecs.surrogatepass_handler)

def get_all_files(dir_path, extension):
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(extension)]

def read_file(path):
    with codecs.open(path, "r", "utf-8", "surrogate_pass") as infile:
        return infile.read()

def write_file(path, content):
    with codecs.open(path, "w", "utf-8", "surrogate_pass") as outfile:
        outfile.write(content)

def read_json(path):
    return json.loads(read_file(path))

def write_json(path, json_object):
    write_file(path, json.dumps(json_object, indent=4, sort_keys=True))

def read_csv(path):
    with codecs.open(path, "r", "utf-8", "sur
