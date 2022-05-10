from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(requests.get(
    "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2", stream=True).content)

def parse_wikipedia_dump(dump: binary_type, output_file: io.BytesIO) -&gt; None:
    decompressor = BZ2Decompressor()
    page = b''
    is_redirect = False
    redirect = b''
    is_start = True
    page_id = 0
    text_value = b''
    extract_text = False
    for line in dump.split(b'\n'):
        line = line.strip()
        if is_start:
            assert line.startswith(b'&lt;mediawiki')
            is_start = False
        elif line.startswith(b'&lt;page&gt;'):
            assert not page and not is_redirect and not redirect and not text_value
            page = line
        elif line.startswith(b'&lt;/page
