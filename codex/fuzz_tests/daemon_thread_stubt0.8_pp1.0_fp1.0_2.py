import sys, threading

def run():
    matrix = [[0 for x in range(n)] for y in range(n)]
    readFile(n, matrix)
    # printMatrix(matrix)
    print "Found paths: "+str(countPaths(matrix))

def rea
