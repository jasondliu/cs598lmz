import codecs
codecs.open("data/colors", "r", "utf8")

import sys
sys.getdefaultencoding()

import json
json.dumps()
json.loads()

import subprocess
subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE)

example = [
        {'name': 'a', 'price': '$5.00'},
        {'name': 'b', 'price': '$4.00'},
        {'name': 'c', 'price': '$3.00'},
        {'name': 'd', 'price': '$2.00'},
        {'name': 'e', 'price': '$1.00'}
    ]


sorted(example, key=lambda item: item["price"].lstrip("$"))

sorted(example, key=lambda item: item["price"].lstrip("$"), reverse=True)


# Tuples and dictionaries

example = (2, 4, 15, 33, 34, 67, 79, 90)

min(example
