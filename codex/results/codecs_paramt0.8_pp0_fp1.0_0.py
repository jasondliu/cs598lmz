import codecs
codecs.register_error("end_of_line", lambda exc: (u"\uFFFD", exc.start + 1))

def parse_word_xml(word_xml_file):
    """
    Parse the word XML file format and returns two lists.
    """
    tree = ET.parse(word_xml_file)
    root = tree.getroot()
    nsmap = root.nsmap
    word_tags = "w"
    word_list = []
    word_numbers = []
    for word in root.iter(qn(root, word_tags)):
        if 'pos' not in word.attrib:
            continue
        word_text = word.text.translate(table)
        pos_tag = word.attrib['pos']
        word_list.append((word_text, pos_tag))
        # Get the word number
        word_numbers.extend([s.attrib['id'] for s in word.iter(qn(root, 's'))])
    return word_list, word_numbers


def parse_sense_key
