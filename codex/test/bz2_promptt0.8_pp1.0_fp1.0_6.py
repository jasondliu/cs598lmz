import bz2
# Test BZ2Decompressor - should be no exception here
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

def clean_line(line):
    try:
        decoded_line = line.decode('utf-8')
        line_array = decoded_line.split(' ')
        cleaned_array = [word.strip() for word in line_array if word != '']
        return cleaned_array
    except:
        return None

def _read_line(filename, i):
    text = ''
    with bz2.BZ2File(filename, 'rb') as archive:
        for j, line in enumerate(archive):
            if j == i:
                text = line
                break
    return text

