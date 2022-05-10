import ctypes
ctypes.cdll.LoadLibrary('/usr/local/cuda/lib64/libcufft.so')

# Load data
infile = open('mri-q-test.dcm', 'rb') # Open in binary mode
dcm_in = dicom.read_file(infile, force=True) # DICOM file decoder and encoder
infile.close()

# Display information about the file
print """Image pixel size %d x %d, pixel spacing %g x %g, slice thickness %g
Image center at %g, %g, %g""" % (dcm_in.Columns, dcm_in.Rows, dcm_in.PixelSpacing[0], dcm_in.PixelSpacing[1], 
                                      dcm_in.SliceThickness, dcm_in.ImagePositionPatient[0], dcm_in.ImagePositionPatient[1], 
                                      dcm_in.ImagePositionPatient[2])

# Convert the image raw data to NumPy array
dcm_arr = np.fromstring(dcm
