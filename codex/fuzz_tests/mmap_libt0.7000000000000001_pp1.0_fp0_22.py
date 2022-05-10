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

replace_file('/etc/ssh/sshd_config.tmp', '/etc/ssh/sshd_config')

with open('/etc/ssh/sshd_config', 'r') as ssh_config:
    mm = mmap.mmap(ssh_config.fileno(), 0, access=mmap.ACCESS_READ)
    if mm.find(b'PermitRootLogin yes') != -1:
        print('***WARNING***')
