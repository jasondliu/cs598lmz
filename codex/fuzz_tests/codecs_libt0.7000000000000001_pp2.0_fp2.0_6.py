import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# test if we are in the top level project directory, if not exit
def in_top_level():
    files = os.listdir('.')
    if 'manage.py' in files and 'tables_init.py' in files and 'wsgi.py' in files and 'requirements.txt' in files and 'README.md' in files:
        return True
    else:
        print 'ERROR: not in top level project directory'
        sys.exit()


# test if a string is an int
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# test if a string is a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# test if a string is a boolean
def is_boolean(s):
    if s == 'True' or s == '
