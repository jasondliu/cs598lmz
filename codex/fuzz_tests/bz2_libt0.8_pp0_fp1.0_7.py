import bz2
bz2.BZ2Decompressor().decompress(output.T[0])

#%%
# For smaller files, you might want to load the entire file
# into a single 1-D array and work with that.
age = np.loadtxt('examples/ex1.csv', delimiter=',', skiprows=1, usecols=[2])
age_out = age > 55

#%%
# The missing_values keyword can be used to specify a different string
# to represent missing values:
data = np.loadtxt('examples/ex5.dat', delimiter='\t',
                    skiprows=1, missing_values='Nothing')

#%%
# By default, invalid entries are skipped, but this can be changed
# with the filling_values keyword:
data = np.loadtxt('examples/ex5.dat', delimiter='\t',
                    skiprows=1, missing_values='Nothing', filling_values=-999)

#%%
# We can also specify what data type we want:
arr = np.array([[1, 2, 3], [4, 5,
