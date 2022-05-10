import types
types.SimpleNamespace
from desc.imsim import compare_obshistid_plots as compare_plots
import os
from astropy.io import fits
from desc.imsim import _fits_utils as f_utils
from desc.imsim import test_utils as tutils
import numpy as np
from scipy.stats import binned_statistic_dd, norm
import unittest
from glob import glob

def compare_instcat_plots(obsHistIdA, obsHistIdB, message=None, png_file=None):
    outfile = png_file
    observations = compare_plots.get_observation_data(obsHistIdA, obsHistIdB)
    for observation in observations:
        for stream in ['visit_ccd_table', 'sensor_table']:
            for num in ['A', 'B']:
                eval("compare_plots.plot_ccd_%s(observation['obsHistId%s'], outfile)" % (stream, num))
                compare_plots.diff_png(outfile
