import codecs
codecs.register_error('ignore', codecs.Codec)

plt.rcParams['font.family'] = 'Times New Roman'

# pylint: disable=invalid-name
# pylint: disable=unused-argument

# set font size
plt.rcParams.update({'font.size': 16})
font = {'size'   : 16}

#--------------------------------------------------------------------
# Utility functions
#--------------------------------------------------------------------

def GetFileName(module, testcase):

	path = "data/" + module + "/" + testcase + ".csv"

	#path = "data/" + module + "/" + testcase + "-temp.csv"
	return path 

def GetRefFile(module, testcase):
	path = "ref/" + module + "/" + testcase
	return path

def GetRefLines(path):

	fp = open(path, 'rb')
	lines = fp.read().splitlines()
	fp.close()

	return lines

def WriteRef(module, testcase, lines, header="labels"):
	path = "
