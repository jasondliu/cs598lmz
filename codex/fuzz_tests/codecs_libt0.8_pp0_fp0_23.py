import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

# For .read()
sys.stdin = codecs.getreader('UTF-8')(sys.stdin)

# For writing the output in a file
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

#For writing the output to the console
#sys.stdout = codecs.getwriter('cp65001')(sys.stdout, 'strict')

#For reading the output
sys.stdout.errors = 'xmlcharrefreplace'
</code>
The above code works fine. I could read the input file, write the output to a file, and I could also read the output file with the chars replaced.
Now I want to store the output in a variable in python and return the output. When I do this, I see some special characters in the output and that makes the output not readable. 
Sample code which does not work
<code>#!/usr/bin/python
# -*- coding: utf-8 -*
