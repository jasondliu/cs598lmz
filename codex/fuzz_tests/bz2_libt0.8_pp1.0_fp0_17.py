import bz2
bz2.compress('S')

import cPickle
cPickle.dumps(0)

import cProfile
cProfile.run('0')

import datetime
datetime.date.today()

import DB
DB.RunQuery('select * from random')

import difflib
difflib.HtmlDiff().make_table('123','1234')

import distutils
distutils.spawn.find_executable('a')

import doctest
doctest.testmod()

import email
email.Message()

import encodings
encodings.aliases.aliases['a']

import htmlentitydefs
htmlentitydefs.name2codepoint['aa']

import hotshot
hotshot.stats.load('a.profile').dump_stats('a.stats')

import json
json.dumps(0)

import libxml2
libxml2.parseFile('a.xml')

import lxml
lxml.etree.parse('a.xml')

import multiprocessing
multiprocessing.cpu_count
