import codecs
codecs.register_error("strict", codecs.ignore_errors)

def main():
	
	'''
	#for i in range(500):
	for i in range(1):
		
		#datfname = 'dat/dat/dat' + str(i) + '.dat'
		datfname = 'dat/dat/dat' + str(i) + '.dat'
		
		print datfname
		
		import os
		if os.path.isfile(datfname):
			print "Skipping " + datfname + "!"
			continue
		
		try:
			print "Fetching: " + datfname + "..."
			dat = fetch(datfname)
			print "Done."
			print "Writing: " + datfname + "..."
			write(datfname, dat)
			print "Done."
		except:
			print "Failed."
		
		
		#break
	''
