import bz2
bz2.decompress(bz2.compress(out))

# %%
def bz2_numpy_save(filename, arr):
    np.save(filename, arr)
    with open(filename, 'rb') as f_in, bz2.BZ2File(filename+'.bz2', 'wb') as f_out:
        f_out.writelines(f_in)
    os.remove(filename)

def bz2_numpy_load(filename):
    with bz2.BZ2File(filename, 'rb') as f_in, open(filename[:-4], 'wb') as f_out:
        f_out.writelines(f_in)
    out = np.load(filename[:-4])
    os.remove(filename[:-4])
    return out

# %%
np.save('test.npy', out)
bz2_numpy_save('test.npy', out)
bz2_numpy_load('test.npy.bz2')

# %%
# Note that
