import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import subprocess
import sys
import pandas
import scipy.stats as stats
import numpy
import scipy.stats
import collections
import itertools
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context(context="paper")
sns.set_style('white')
sns.set_style('ticks')
import re
import os
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument( '--inputMutationMatrix', type=str, required=True )
	parser.add_argument( '--inputMutationalSignature', type=str, required=True )
	parser.add_argument( '--outputDirectory', type=str, required=True )
	parser.add_argument( '--outputFileNameStub', type=str, required=True )
	parser
