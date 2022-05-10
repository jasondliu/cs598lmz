import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

def gexf_to_graph(gexf_file, directed=False):
    """
    Load a graph from a gexf file.
    """
    graph = nx.Graph(directed=directed)
    parser = et.XMLParser(encoding='utf-8')
    tree = et.parse(gexf_file, parser=parser)
    root = tree.getroot()
    graph.graph['name'] = root.attrib['title']
    graph.graph['creator'] = root.attrib['creator']
    graph.graph['description'] = root.attrib['description']

    for node in root.iter('node'):
        id = node.attrib['id']
        label = node.attrib['label']
        graph.add_node(id, label=label)

    for edge in root.iter('edge'):
        source = edge.attrib['source']
        target = edge.attrib['target']
        weight = edge.attrib['weight']
        graph.add_
