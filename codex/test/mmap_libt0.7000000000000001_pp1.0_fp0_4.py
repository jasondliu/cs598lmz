import mmap
import sys
import os
import math

def dict2col(col_name,dict):
	return [dict[k] for k in col_name]

def get_ncol(data,col_name):
	result = []
	for key in col_name:
		result.append(data[key])
	return result

def get_nlin(data,lin_name):
	result = []
	for key in lin_name:
		result.append(data[key])
	return result

def get_col(data,col_name):
	result = []
	for i in range(len(data)):
		result.append(data[i][col_name])
	return result

def get_lin(data,lin_name):
	return data[lin_name]

def get_col_header(data):
	return data[0]

def get_lin_header(data):
	return [k for k in data]

