import mmap
import numpy as np
import pdb
import re
import sys
import time
import traceback
import warnings
import yaml

from . import aps
from . import raster
from . import util

from . import cli

###############################################################################

def main():
    """
    The main function.
    """

    # Parse command-line arguments.
    args = cli.parse_args()

    # Read the configuration file.
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    # Create the output directory if it doesn't already exist.
    os.makedirs(config["output_dir"], exist_ok=True)

    # Load the images.
    images = []
    for image_file in config["images"]:
        print("Loading {}...".format(image_file))
        image = raster.load(image_file)
        images.append(image)

    # Load the image mask.
    if "image_mask" in config:
        print("Loading {}...".
