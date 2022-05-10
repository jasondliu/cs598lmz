import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
#
# Initializations
#
plt.ion()
#
# Read the data from the file
#
f = open('../data/evtdata.txt','r')
#
# Read the data into a numpy array
#
print('Reading the data ...')
for line in f:
  #
  # Read the first line and get the number of data values
  #
  if 'Npoints' in line:
    Npoints = int(line.split(':')[1])
    print('Npoints = ', Npoints)
  #
  # Read the second line and get the number of detectors
  #
  if 'Ndet' in line:
    Ndet = int(line.split(':')[1])
    print('Ndet = ', Ndet)
  #
  # Read the third line and get the number of columns
  #
  if 'Ncols' in line:
    Ncols = int(line.split(':')[1])
    print('Ncol
