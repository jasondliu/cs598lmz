import sys, threading
threading.Thread(target=lambda:sys.stdout.write('Threading\n')).start()

# Importing Modules
import sys
print('\n'.join(sys.path))

# The dir() Function
import sys
print(dir(sys))
print(dir())

# Packages
# __init__.py

# Standard Library Modules
# The sys Module
import sys
print(sys.platform)
print(sys.maxsize)
print(sys.path)
print(sys.version)

# The os Module
import os
print(os.getcwd())
print(os.urandom(25))

# The shutil Module
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

# The glob Module
import glob
print(glob.glob('*.py'))

# The argparse Module
import argparse
parser = argparse.ArgumentParser(description='Search some files')
