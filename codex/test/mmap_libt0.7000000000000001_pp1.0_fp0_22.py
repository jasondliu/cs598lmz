import mmap

def get_env_var(name):
    return os.environ.get(name, name)

def format_env_var(line):
    return line.format(**{k: get_env_var(k) for k in os.environ.keys()})

def replace_file(source, destination):
    with open(source, 'r') as source_file:
        with open(destination, 'w') as destination_file:
            destination_file.writelines(
                format_env_var(line) for line in source_file)
    os.chmod(destination, 0o600)

