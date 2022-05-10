import mmap
import tempfile
import os
import os.path
import sys
from stat import *

from config import *

def rmfile( elem, mask, names ):
	for i in names:
		path = os.path.join( elem, i )
		print path
		os.unlink( path )

def unzip( zipName ):
	import zipfile
	z = zipfile.ZipFile( zipName )
	for path in z.namelist():
		z.extract( path, 'core' )

def searchfile( pattern, root = os.path.curdir ):
	names = []
	for name in os.listdir( root ):
		if os.path.isfile( os.path.join( root, name ) ):
			if re.match( pattern, name ):
				names.append( name )
		elif os.path.isdir( os.path.join( root, name ) ):
			names.extend( searchfile( pattern, os.path.join( root, name
