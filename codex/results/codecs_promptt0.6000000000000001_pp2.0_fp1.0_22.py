import codecs
# Test codecs.register_error('replace_with_space', replace_with_space)
# Test codecs.register_error('ignore', ignore_encoding_error)

def clean_sentence(sentence):
    sentence = sentence.replace("\n", "").replace("\r", "")
    sentence = sentence.replace(",", " , ").replace(".", " . ").replace("!", " ! ").replace("?", " ? ")
    sentence = sentence.replace(":", " : ").replace(";", " ; ").replace("\"", " \" ").replace("\'", " \' ")
    sentence = sentence.replace("(", " ( ").replace(")", " ) ").replace("{", " { ").replace("}", " } ")
    sentence = sentence.replace("[", " [ ").replace("]", " ] ").replace("/", " / ").replace("+", " + ")
    sentence = sentence.replace("-", " - ").replace("*", " * ").replace("&", " & ").replace("%", " % ")
    sentence = sentence
