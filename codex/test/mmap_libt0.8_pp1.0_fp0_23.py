import mmap
import sys
import os

# Constants
BLOCK_SIZE = 256
DEFAULT_FILE = "disk.bin"

# Function prototypes
def getFileBlock(blockIndex, file):
    file.seek(blockIndex * BLOCK_SIZE)
    return file.read(BLOCK_SIZE)

def getBlock(blockIndex):
    return getFileBlock(blockIndex, mm)

def getFileSize():
    global mm
    mm.seek(0,2)
    return mm.tell()

def getFreeListBlock():
    superBlock = getBlock(0)
    startOfFreeList = unpack("<I", superBlock[4:8])[0]
    return getBlock(startOfFreeList)

def printFreeList():
    freeListBlock = getFreeListBlock()
    freeList = unpack("<" + 16 * "I", freeListBlock)
