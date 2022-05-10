import bz2
bz2.decompress(b)
s_ut.assert_equals(bz2.decompress(b), 'Compressed File')

#'Pickle' is a standard library for object serialization. 
#It is used for storing python objects for later re-use.
#You can use the module to load up a python object, 
#and then load it again at a later time. 
#This is useful for making game state stored as a python object, 
#or save files.
import pickle
pickle.loads(b'\x80\x03]q\x00.')
s_ut.assert_equals(pickle.loads(b'\x80\x03]q\x00.'), [])

#'URLlib' is a standard library for fetching webpages over HTTP. 
#You can use this to build a simple spider similar to a search engine.
from urllib.request import urlopen
a = urlopen('http://python.org')
s_ut.assert_equals(a.read().decode(), '<!doctype html>
