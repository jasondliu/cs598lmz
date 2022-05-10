import codecs
codecs.register_error('strict', codecs.ignore_errors)
text = open('text.txt','r',encoding='utf-8', errors='ignore').read()
text = text.lower()
patterns = {"[á]": "a",
            "[é]": "e",
            "[í]": "i",
            "[ó]": "o",
            "[ú]": "u"}

for a,b in patterns.items():
    text = re.sub(a, b, text)
# Remove citations
text = re.sub(r"\[\d+\]", "", text)
# Remove punctuation
text = re.sub(r"\.", "", text)
text = re.sub(r"\,", "", text)
text = re.sub(r"\;", "", text)
text = re.sub(r"\:", "", text)
text = re.sub(r"\?", "", text)
text = re.sub(r"\¿", "", text)
text = re.sub(r"\¡", "", text
