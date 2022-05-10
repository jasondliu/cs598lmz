import threading
threading.stack_size(2**27)

# Find the right tag kind
def kind(n, k):
    if k in n.attrib:
        return n.attrib[k]
    else:
        return ''

def super_print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def count_tags(filename):
    with open(filename, 'r') as osm:
        osm_file = osm.read()
        osm = ET.fromstring(osm_file)
        tags = {}
        for event, elem in ET.iterparse(filename, events=('start', 'end')):
            if event == 'start':
                if elem.tag not in tags:
                    tags[elem.tag] = 1
                else:
                    tags[elem.tag] += 1
    return tags

# Count the number of times each element appears in the file
def count_elements(filename):
    elements = {}
