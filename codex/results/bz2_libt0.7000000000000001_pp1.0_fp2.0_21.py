import bz2
bz2.BZ2File.read = bz2.BZ2File.readline
import pandas as pd

import os
import argparse
import logging
import json
import sys


def get_args():
    """get command line arguments"""
    parser = argparse.ArgumentParser(
        description="""
        Extracts relevant information from a bz2 file."""
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="input file with Amazon reviews",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output file with extracted information",
        required=True,
    )
    parser.add_argument(
        "-p",
        "--parser",
        type=str,
        help="parser to be used to extract information from reviews",
        required=True,
    )
    parser.add_argument(
        "-k",
        "--keywords",
        type=str,
       
