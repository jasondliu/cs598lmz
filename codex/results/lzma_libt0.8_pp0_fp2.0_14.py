import lzma
lzma.open(data_file)

def parse_xml_file(data_file):
    """
    Reads XML file and returns a dict dimension_name->[list of dimension entries
    (name, class, level, parent_id)] in a format that I can just feed into
    to_graph.
    """
    context = etree.iterparse(data_file, events=('start', 'end'))
    context = iter(context)
    event, root = context.next()

    ret = {}

    for event, elem in context:
        if event == 'end':
            if elem.tag == 'dimension':
                dim_name = elem.get('name')
                ret[dim_name] = []
            elif elem.tag == 'dimensionEntry':
                parent_id = elem.get('parentId')
                if parent_id is None:
                    parent_id = '1'
                ret[dim_name].append(
                    DimensionEntry(elem.get('name'), elem.get('class'),
                                   elem.get('level
