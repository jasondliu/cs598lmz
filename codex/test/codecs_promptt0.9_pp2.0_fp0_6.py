import codecs
# Test codecs.register_error()
def search_function(encoding):
    if encoding == "ascii":
        return codecs.lookup("latin1")
    if encoding == "latin-1":
        return codecs.lookup("latin-1")

codecs.register_error("replace_char", codecs.replace_errors)
c='a'.encode('utf-8', 'replace')

# Sputnik 
words_set = set()
