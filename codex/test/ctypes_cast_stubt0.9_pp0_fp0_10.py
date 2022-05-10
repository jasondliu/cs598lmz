import ctypes
ctypes.cast(0,ctypes.py_object)
#Xlib.display.Display()

#-------------------------------------------------------------------------------------
#=====================================================================================

#  QR code scanner part
#  input : filename
#  output: data (frame)
#  function : 1. Read all QR code from the png file
#             2. Read data from received file

#=====================================================================================
#-------------------------------------------------------------------------------------

def QRreader(filename):
    
    # Read filename
    fr = open(filename, 'r')
    # Read data (frame)
    data = fr.read()
    fr.close()
    
    return data

#-------------------------------------------------------------------------------------
#=====================================================================================

#  Cylce part
#  input : fdata (output of QRreader)
#  output: (probability, label) 
#  function : 1. Asses data and return the best classifier and probability
#             2. Return data to .txt file

#=====================================================================================
#-------------------------------------------------------------------------------------

