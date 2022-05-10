import _struct
import _math
import collections
import re
import math
import sys

#Function to print to stderr
verbose=False
def debug(string):
	if verbose:
		print(string,file=sys.stderr)

#Function to get the untransformed position of a subsegment
def get_positions(m):
	positions=[]
	for i in range(m.shape[0]):
		positions.append(_struct.unpack('d',m[i,0:8]))
	return(positions)

#======================================================================
# Function to find the recommended radius
#======================================================================
def recommend_radius(types,FL,dlambda=0.01,maxlambda=1.0,maxiter=20,tol=1.0e-10):
	#Default to 0 if no types argument supplied
	if not 'types' in locals():
		types=[]
	
	if isinstance(types,str):
		types=[types]

