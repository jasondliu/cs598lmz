from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress
del decompress


def system(cmd):
    print(cmd)
    os.system(cmd)


###

def prepare_workspace():
    system('git config user.email "bruno.de.oliveira.moreira@gmail.com"')
    system('git config user.name "Bruno de Oliveira Moreira"')
    system('git config --global push.default simple')


def get_platform():
    if sys.platform.startswith('linux'):
        return 'linux'
    elif sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
        return 'win'
    else:
        raise RuntimeError('Unsupported platform: %s' % sys.platform)


def clone_repo(url, path):
    if os.path.exists(path):
        return
    system('git clone %s %s' % (url, path))


def update_repo(path):
    if not os.path.exists(path):
        return
