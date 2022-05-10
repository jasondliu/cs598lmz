import _struct
import time
import pickle
import sys
import numpy as np


#Parameters from the paper
numAnts = 50 #number of ants per patch
numTweak1 = 12 #number of circles in first tweak
numTweak2 = 6 #number of circles in second tweak
numTweak3 = 3 #number of circles in third tweak
numTweak4 = 1 #number of circles in fourth tweak
circValue = 2 #value (radius) of each circle
maxNumPatches = 100 #max number of patches on screen at any one time
numTrials = 400 #number of trials in a block

#Assign trial types
tweaks = [numTweak1, numTweak2, numTweak3, numTweak4]
blockTrials = np.fmod(np.arange(numTrials), tweaks[0]+tweaks[1]+tweaks[2]+tweaks[3])

#Create a circular patch for the center of the screen
patch = psychopy.visual.Circle(win = win, radius = 0.05, edges = 128)

#Create a text object for
