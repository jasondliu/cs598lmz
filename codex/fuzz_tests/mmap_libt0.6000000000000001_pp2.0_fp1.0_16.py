import mmap
import sys

def main():
	try:
		needle = sys.argv[1]
		haystack = sys.argv[2]
	except:
		print >>sys.stderr, "Usage: %s <needle> <haystack>" % sys.argv[0]
		sys.exit(1)

	with open(haystack, 'r') as f:
		s = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
		if s.find(needle) != -1:
			print "Found!"
		else:
			print "Not found"

if __name__ == '__main__':
	main()
