import lzma
lzma.open

# We move the code to fold_modes.py, to be executed on the client machine
# in the same directory. This avoids an issue with the sys.path not being
# able to include this directory, as there is no __init__.py.
# This is not a problem, it's just a bit ugly.
import os.path
cp = os.path.dirname(__file__)
fold_modes = os.path.join(cp, "fold_modes.py")
