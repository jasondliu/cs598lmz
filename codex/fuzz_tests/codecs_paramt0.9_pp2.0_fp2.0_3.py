import codecs
codecs.register_error('replace_ae', lambda error: \
                 (u"ae" if error.object[error.start]==u"\xc4" else u"Ae") + error.object[error.start+1:error.end], )

user_re = re.compile("user_?name1?=([^&\s]+)")
file = open("/var/log/apache2/access.log")
for line in file:
    match = user_re.search(line)
    if match != None:
        print match.group(1).replace("+"," ").decode("utf-8", "replace_ae")
