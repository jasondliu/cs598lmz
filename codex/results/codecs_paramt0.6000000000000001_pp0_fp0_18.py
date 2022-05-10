import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for child in root:
        for each in child:
            if each.text is None:
                each.text = ""
            each.text = each.text.strip()
    return root

def get_text(root):
    text = []
    for child in root:
        for each in child:
            text.append(each.text)
    return text

def get_list(text):
    new_list = []
    for each in text:
        each = each.split()
        for word in each:
            if word != "":
                new_list.append(word)
    return new_list

def get_count(new_list):
    count = {}
    for word in new_list:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

def get_freq(count):
   
