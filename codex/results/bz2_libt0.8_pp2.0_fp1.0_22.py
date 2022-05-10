import bz2
bz2_file = bz2.BZ2File('./data/20170325_sample_data.json.bz2')
data = [json.loads(line) for line in bz2_file]
len(data)

'''
Produce the top 10 nodes based on the number of outgoing edges.
'''
#def top10_outgoing_nodes():

nodes = {}
for line in data:
    if line['type'] == 'RECEIVE':
        from_node = line['from_node']
        to_node = line['to_node']
        if from_node in nodes:
            nodes[from_node] += 1
        else:
            nodes[from_node] = 1

nodes

# Use the Counter of collections for the same
nodes = {}
from collections import Counter
for line in data:
    if line['type'] == 'RECEIVE':
        from_node = line['from_node']
        to_node = line['to_node']
        if from_node in nodes:
            nodes[from_node]
