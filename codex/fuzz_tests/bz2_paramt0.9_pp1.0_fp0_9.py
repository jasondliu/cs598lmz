from bz2 import BZ2Decompressor
BZ2Decompressor.get_unused_data = lambda self: None 

from convert_text2wav import *
from transcriber import *
from extract_text import *

from common_utils import load_json, save_json


def main():
	opt = docopt("""
	    Usage:
	        create_transcripts.py <template_file> <vocab_file> <model_dir> <w2i_file_name> <idx_file_name>  <test_file> <data_dir> <output_dir> [options]
	        create_transcripts.py -h | --help
	    Options:
	        -r, --replace    Replace generated text and download
	        -h, --help       This help
	""")

	template_file = opt['<template_file>']
	model_dir = opt['<model_dir>']
	test_file = opt['<test_file>']
	w2i_file_name = opt['<w2i_file_name>']
	idx_file_name = opt['<id
