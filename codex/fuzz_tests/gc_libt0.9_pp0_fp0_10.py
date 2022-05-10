import gc, weakref, weakrefcallbackex

import gc, weakrefcallbackex

#The following is to test general case, as suggested in comments. It will be successful if the refcounts are 0 and 3.

import weakrefcallbackex
a = weakrefcallbackex.b()
ref = weakrefcallbackex.weakref.ref(a,callback=weakrefcallbackex.f)
del a
print(gc.collect())
print(ref())
assert ref() == None, "This must be None."

#The following is to test specific case to show my problem, as mentioned in the question.

import weakrefcallbackex
import os
ref = weakrefcallbackex.weakref.ref(weakrefcallbackex.b(),callback=weakrefcallbackex.f)
os.system('dir\\weakrefdir.dir\\weakrefdir2\\weakrefdir3\\weakrefdir4\\weakrefdir5\\weakrefdir6\\weakrefdir7\\weakrefdir8\\weakrefdir
