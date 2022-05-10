import mmap, os
import scipy.io as sio

datasetPath = 'datasets/'
datasetName = 'outdoor'
datasetFile = datasetPath + datasetName + '.txt'
datasetPathFS = datasetPath + datasetName + '_fs'
datasetPathFeatures = datasetPath + datasetName + '_features'
datasetPathOutput = datasetPath + datasetName + '_output'
datasetPathSortedFeatures = datasetPath + datasetName + '_sorted_features'

try:
    os.system('mkdir ' + datasetPathFS + ' ' + datasetPathFeatures)
except OSError:
    pass

try:
    os.system('rm -r ' + datasetPathOutput)
except OSError:
    pass

try:
    os.system('mkdir ' + datasetPathOutput)
except OSError:
    pass

with open(datasetFile, 'r') as fin:
    for line in fin:
        filename = line.strip()
        raw = cv2.im
