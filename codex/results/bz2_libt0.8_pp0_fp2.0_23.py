import bz2
bz2.__version__

# ======================================================================
# %% Test Data
# ======================================================================

filename = os.path.join('..', 'tests', 'data')


# ======================================================================
# %% Functions
# ======================================================================

# ----------------------------------------------------------------------
# %% main
# ----------------------------------------------------------------------
def test_bz2():
    bz2.compress(''.encode())
    bz2.compress(' '.encode())
    bz2.compress('\n'.encode())
    bz2.compress('\n\n\n'.encode())
    bz2.compress(b'spam')
    bz2.compress(b'eggs')
    bz2.compress(b'Spam and Eggs')
    bz2.compress(b'Spam, spam, spam and eggs')
    bz2.compress(b'Spam, spam, spam, spam, spam, spam, spam and eggs')

    with open(filename, 'rb') as f:
        data = f.read()
        bz2.compress
