import sys, threading

def run():
    global action
    action()

def upgrade():
    action = run
    min_version = getattr(__bootstrap__, "bootstrap_mindist", -1)
    cur_version = getattr(__bootstrap__, "bootstrap_curdist", -1)
    file_name = getattr(__bootstrap__, "bootstrap_filename", "")
    base_dir = os.getcwd()
    tb = sys.exc_info()
    if file_name == os.path.join(base_dir, "easy_install.py"):
        import __main__
        main_dir = os.path.dirname(os.path.abspath(__main__.__file__))
        base_dir = os.path.dirname(os.path.dirname(main_dir))
    old_dir = os.getcwd()
    try:
        os.chdir(base_dir)
        if not os.path.exists(file_name):
            if file_name == os.path.join(base_dir, "easy
