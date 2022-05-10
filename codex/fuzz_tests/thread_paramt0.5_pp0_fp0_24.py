import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def get_env_var(name):
    try:
        return os.environ[name]
    except KeyError:
        print("${} must be set".format(name))
        sys.exit(1)

def get_env_var_int(name):
    try:
        return int(get_env_var(name))
    except ValueError:
        print("${} must be set to an integer".format(name))
        sys.exit(1)

def get_env_var_bool(name):
    try:
        return get_env_var(name).lower() == 'true'
    except ValueError:
        print("${} must be set to a bool".format(name))
        sys.exit(1)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING
