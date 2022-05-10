import codecs
codecs.encode(test.word,'hex')
</code>
and I got error:
<code>AttributeError: 'Pair' object has no attribute 'word'
</code>
Thus I wonder where is my word list and how do I get it from this tree. The <code>Pairs.word</code> gave me error as well:
<code>AttributeError: 'tuple' object has no attribute 'word'
</code>
P.S. there is no error when I read the file <code>Potsdam book</code>
UPDATE:
this is my code (I changed the file to another because the first file was too long):
<code>from anytree import NodeMixin
import anytree
import codecs

# Created pairs.txt file. First column is id, second tuple, third word.
f = open("pairs_test.txt", 'r')

data = f.readlines()
data = [x.strip() for x in data]
basepair = NodeMixin()
pair_dict = {}
for d in data:
    d = d.split()
    pair
