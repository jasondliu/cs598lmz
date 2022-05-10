import threading
threading.stack_size(2**27)
import sys
import glob
import pickle
sys.path.append('../../../../venv/Lib/site-packages')

# Own Tensorflow folder
sys.path.append('../../../../03_Code/06_Tensorflow/')

# Import own functions
from CNN_Functions import *

# Import functions from other folders
sys.path.append('../../../../01_Generate_Grid/01_Generate_Points/')
import Points_Within_Radius as PWR

# Import functions from other folders
sys.path.append('../../../../02_Generate_Data/')
import Basic_Functions as BF

# Define global variables
global model
global graph

# Get the GPU to be used
GPU = BF.get_gpu()

# Define the name of the model
Model_Name = 'CNN_1'

# Define the batch size
Batch_Size = 64

# Define the number of classes
Num_Classes = 2

# Define the number of features

