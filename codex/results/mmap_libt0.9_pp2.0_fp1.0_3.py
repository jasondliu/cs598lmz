import mmap
import sys

if len(sys.argv) < 3:
    print "Usage:  python %s [input_pipeline.dot] [output_pipeline.vm]" % __file__
    print "                                                        "
    print "  Writes the gvvm mapping of the original pipeline to   "
 
