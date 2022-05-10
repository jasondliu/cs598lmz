import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
#	Constants
#

#	This is the main directory for the project.
#	All other directories are relative to this one.
#	This directory must exist and be writeable.
MAIN_DIR = "/home/james/projects/python/thesaurus/"

#	This is the directory where the output files
#	are written.
OUTPUT_DIR = MAIN_DIR + "output/"

#	This is the directory where the log files are
#	written.
LOG_DIR = MAIN_DIR + "log/"

#	This is the directory where the source files
#	are read from.
SOURCE_DIR = MAIN_DIR + "source/"

#	This is the directory where the template files
#	are read from.
TEMPLATE_DIR = MAIN_DIR + "template/"

#	This is the directory where the SQL files
#	are read from.
SQL_DIR = MAIN_DIR + "sql/"

#	This is the directory where the XML files
#	
