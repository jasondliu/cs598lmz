import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# Import modules
import numpy as np
import matplotlib.pyplot as plt

# Import classes
from classes.class_data import Data
from classes.class_model import Model
from classes.class_predictor import Predictor
from classes.class_trainer import Trainer
from classes.class_visualizer import Visualizer

# Import functions
from functions.function_data import generate_data
from functions.function_model import generate_model
from functions.function_predictor import generate_predictor
from functions.function_trainer import generate_trainer
from functions.function_visualizer import generate_visualizer

# Import parameters
from parameters.parameters_data import data_parameters
from parameters.parameters_model import model_parameters
from parameters.parameters_predictor import predictor_parameters
from parameters.parameters_trainer import trainer_parameters
from parameters.parameters_visualizer import visualizer_parameters

# Import data
