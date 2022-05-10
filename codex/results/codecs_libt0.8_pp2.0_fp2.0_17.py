import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

"""
To convert an RTF file to text, do this:

1) Run the script on the RTF file using the "rtf2txt" command line switch.
   For example:

      python rtfobj.py -rtf2txt sample.rtf sample.txt

2) This converts the RTF file to text.  The RTF format is quite simple
   and easy to understand, so you could write your own RTF reader if you wanted.
"""

"""
The idea is that an RTF file is a sequence of groups.  Each group
has its own set of properties and possibly a group of other groups.

A group begins with an open brace, has a series of properties
(possibly none), and ends with a close brace.  After this the
text, if any, of the group follows.  If the group has other groups
nested inside it, then they follow.

Each property is a backslash followed by a keyword (a word or two words)
possibly followed by an
