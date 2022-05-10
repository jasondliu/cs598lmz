import ctypes
ctypes.cast(x, ctypes.py_object).value

#%%
# Import the module
import astropy.io.fits as pyfits

# Open the file using the astropy.io.fits module
infile = pyfits.open('NGC5236_FUV.fits')

# Print the header
print(infile[0].header)

# Close the file
infile.close()

#%%
# Import the module
import astropy.io.fits as pyfits

# Open the file using the astropy.io.fits module
infile = pyfits.open('NGC5236_FUV.fits')

# Get the data
data = infile[0].data

# Print the data
print(data)

# Close the file
infile.close()

#%%
# Import the module
import astropy.io.fits as pyfits

# Open the file using the astropy.io.fits module
infile = pyfits.open('NGC5236_FUV.fits')

# Get the header
header = infile[0].header


