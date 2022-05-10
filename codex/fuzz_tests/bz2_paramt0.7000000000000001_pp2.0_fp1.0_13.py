from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = ctypes.windll.kernel32.GlobalAlloc

#
#The main function
#
def main():
	#
	#Connecting to the file
	#
	doctext = open('doc.txt','w+')

	#
	#The main loop for the function
	#
	while True:
		#
		#Reading the file
		#
		try:
			#
			#Reading the file
			#
			text = open('doc.bz2', 'rb').read()
			#
			#Try to decompress the file
			#
			try:
				#
				#Decompressing the file
				#
				decompressed = bz2.decompress(text)
				#
				#Printing the file
				#
				print decompressed
				#
				#Exiting the program
			
