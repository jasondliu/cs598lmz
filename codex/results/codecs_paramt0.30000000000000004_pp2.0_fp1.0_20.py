import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_fname(fname, n=0):
    if n == 0:
        return fname
    else:
        return fname + '.' + str(n)

def get_next_fname(fname):
    n = 0
    while os.path.exists(get_fname(fname, n)):
        n += 1
    return get_fname(fname, n)

def get_fname_and_move(fname):
    fname = get_next_fname(fname)
    shutil.move(fname, fname + '.bak')
    return fname

def get_fname_and_copy(fname):
    fname = get_next_fname(fname)
    shutil.copyfile(fname, fname + '.bak')
    return fname

def get_fname_and_copy_to(fname, to):
    shutil.copyfile(fname, to)

def get_fname
