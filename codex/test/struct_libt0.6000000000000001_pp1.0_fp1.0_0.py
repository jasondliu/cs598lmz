import _struct

def main():
    
    # open the file, and create the file object f
    f = open('data.bin', 'rb')
    
    # read the contents of the file into a string
    file_content = f.read()
    
    # close the file
    f.close()
    
    # get the size of the file
    size = os.path.getsize('data.bin')
    
    # create a list to store the data
    data = []
    
    # unpack the file content and store in our list
    for i in range(0, size, 4):
        val = _struct.unpack('f', file_content[i:i+4])
        data.append(val[0])
    
    # display the contents of the list
    print('Data: ' + repr(data))

