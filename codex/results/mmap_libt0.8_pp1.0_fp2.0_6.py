import mmap
import os
import sys

def streamFiles(prefix, suffix, directory, numOfFiles):
    # Create the file names from the prefix, suffix, directory and number of files
    fileNames = ['{}{}{}{}'.format(prefix, i, suffix, directory) for i in range(numOfFiles)]
    currentLoadedFile = 0
    fileObjects = []
    # Get each file
    for fileName in fileNames:
        # If this file exists
        if os.path.exists(fileName):
            # Open the file and add it to the list of file objects
            try:
                fileObjects.append(open(fileName))
            except:
                print('Error opening file {}'.format(fileName))

    fileObject = fileObjects[currentLoadedFile]
    if fileObject:
        # Memory map the file
        memoryMappedFile = mmap.mmap(fileObject.fileno(), 0, access=mmap.ACCESS_READ)
        currentLine = 0
        # Keep reading lines until it gets to the end of the file
        while True:
