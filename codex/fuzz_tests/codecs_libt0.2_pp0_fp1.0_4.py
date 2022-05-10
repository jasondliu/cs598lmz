import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
# Import the necessary packages
import numpy as np
import argparse
import cv2
import os

#%%
# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-c", "--config", required=True,
	help="path to yolo config file")
ap.add_argument("-w", "--weights", required=True,
	help="path to yolo pre-trained weights")
ap.add_argument("-cl", "--classes", required=True,
	help="path to text file containing class names")
args = vars(ap.parse_args())

#%%
# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()

