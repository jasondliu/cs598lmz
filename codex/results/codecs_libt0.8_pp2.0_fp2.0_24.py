import codecs
codecs.BOM_UTF8

#define the opening and closing tags
opening_tag = r'<\w*>'
closing_tag = r'</\w*>'

def tokenize(text,language):
    """
    This function returns a list of sentences, each sentence is a tuple that contains a list of tokens.    
    """
    if language == 'english':
        re_sentence = re.compile(r'(?<=[^A-Z].[.?]) +(?=[A-Z])')
        re_token = re.compile(r'[\w\.,]+')
        re_space = re.compile(r'^\s+')
    if language == 'dutch':
        re_sentence = re.compile(r'(?<=[^A-Z].[.?]) +(?=[A-Z])')
        re_token = re.compile(r'[\w\.,]+')
        re_space = re.compile(r'^\s+')
    if language == 'french':
       
