import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\n")).start()
import os
import time
import shutil
# global variables
# options for the project
#        -outDir = "output"
#        -outFile = "default.txt"
#        -inDir = "input"
#        -inFile = "default.txt"
#        -logFile = "log.txt"
#        -logDir = "log"
#        -mode = "d"

outDir = "output"
outFile = "default.txt"
inDir = "input"
inFile = "default.txt"
logFile = "log"
logDir = "log"
mode = "d"


# function definitions
# function to check for the output directory and create it if it doesn't exist
def setUpDir(log, mode):
    log.write("Setting up output Directory\n")
    if not os.path.exists(outDir):
            log.write("Directory does not exist, creating it\n")
            os.mkdir(outDir)
    else:
        # check if
