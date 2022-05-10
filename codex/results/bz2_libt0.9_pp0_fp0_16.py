import bz2
bz2.open?

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import sys
sys.path.append('../src')
import localmodule


# Define constants
dataset_name = localmodule.get_dataset_name()
aug_kinds = ["all", "all-but-noise", "none"]
units = localmodule.get_units()
n_threshs = 201
thresh_max = 2
bg_snrs = [5, 10, 15, 20]
script_name = "036_evaluate-bzip2-convnet-pcen-ntt-add-noise.py"
script_str = script_name[:3]
script_folder =  script_name[:-3]


# Create folder.
os.makedirs(script_folder, exist_ok=True)
sbatch_dir = os.path.join(script_folder, "sbatch")
os.makedirs(sbatch_dir, exist_ok=True)
slurm_dir = os
