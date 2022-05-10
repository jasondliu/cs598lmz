import mmap
import os
import shutil

# are we using nwjs?
nwjs = os.path.isdir(os.path.join(os.path.abspath("."),"distrib"))


# make a copy of the current settings file
from stat import ST_MTIME
def write_new_settings():
    # path to the old settings file
    settings_file = os.path.join(os.path.abspath("."),"data","settings.ini")
    if os.path.isfile(settings_file):
        # copy the settings file
        shutil.copyfile(settings_file, os.path.join(os.path.abspath("."),"settings.ini"))
        # get the os mtime of the file
        os.utime(settings_file, (os.stat(settings_file)[ST_MTIME],)*2)
    else:
        print("warning: settings file not found")
        pass
    return settings_file

