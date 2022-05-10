import gc, weakref


#the database
#use a dict because we want to be able to get any variable by key
#but also because we want to be able to insert new ones
variables = {}

#the number of variables
#this is needed for the global variable numbering algorithm
global_id = 0

#the global variable numbering algorithm
#returns an identifier for a variable
def get_variable(var):
	global global_id
	global variables
	if var in variables:
		return variables[var]
	else:
		global_id += 1
		variables[var] = global_id
		return global_id

#we use weakref here, because we want to be able to delete entries
#but we also want to use the same key for different types of objects
#the weakrefs are held in a list, because we need to iterate over them
#for gc (we couldn't do that with a set for example)
dictionaries = []

#the dictionary numbering algorithm
#returns a dictionary identifier
def get_dictionary(d):
	global dictionaries
