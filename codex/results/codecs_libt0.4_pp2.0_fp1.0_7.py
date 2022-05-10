import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def get_file_path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

def get_file_content(filename):
    file = open(get_file_path(filename), 'r')
    content = file.read()
    file.close()
    return content

def get_file_content_list(filename):
    file = open(get_file_path(filename), 'r')
    content = file.readlines()
    file.close()
    return content

def save_file(filename, content):
    file = open(get_file_path(filename), 'w')
    file.write(content)
    file.close()

def save_file_list(filename, content):
    file = open(get_file_path(filename), 'w')
    file.writelines(content)
    file.close()

def get_file_
