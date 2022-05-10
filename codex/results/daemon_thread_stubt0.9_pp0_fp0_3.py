import sys, threading

def run():
    ## Set up the global variables.
    global binList, binDict, wordList, wordDict
    
    ## Initialize the binary search list and dict.
    binDict = {}
    binList = []
    for i in range(len(wordList)):
        binDict[i] = wordList[i]
        binList.append((i, wordList[i]))
    
    ## Begin timing.
    binaryListStart = time.perf_counter_ns()
    for i in range(len(wordList)):
        toFind = i // 2
        binarySearchList(binList, False, (toFind, "test"))

    binaryDictStart = time.perf_counter_ns()
    for i in range(len(wordList)):
        toFind = i // 2
        binarySearchList(binDict, True, toFind)

    timeBinaryList = binaryDictStart - binaryListStart
    timeBinaryDict = time.perf_counter_ns() - binaryDictStart

    print("Binary Search Times:", time
