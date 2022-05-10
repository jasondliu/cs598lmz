import codecs
codecs.register_error('replace_with_space', replace_with_space)

pre_expand = re.compile(r'\s+')
tab_expand=re.compile(r'\t+')
hashtag = re.compile(r'#[^\s]+\s*')
mention = re.compile(r'@\w+')
url_re = """(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
url = re.compile(url_re)
more_hashtag = re.compile(r'
