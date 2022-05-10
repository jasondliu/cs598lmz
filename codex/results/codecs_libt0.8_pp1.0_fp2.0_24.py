import codecs
codecs.open('file.py', 'w', encoding='utf-8')
</code>
this is a file I created with the Sublime Text 2 editor, and it encodes the characters using the UTF-8 format. Now I want to be able to remove all of the non-ASCII characters from the file.
I've tried this method, but it doesn't work for me.
I think that the problem might be that my file is encoded differently than the file in the question I've linked to.
I've found this code, which removes the accentuated characters, but doesn't solve my problem:
<code>import re 

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
</code>
Could you please help me find a solution to this problem?
This is the file I want to process:
<code># -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:32:50 2015

@author: s
"""
from gens
