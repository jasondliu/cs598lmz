import socketserver
import argparse

def translate_count(data):
    ascii_data = int_to_ascii(data)
    words = ascii_data.split()
    translated_words = []
    for word in words:
        translated_words.append(translate_count_word(word))
    return ' '.join(translated_words)

def int_to_ascii(data):
    return ''.join([chr(int(datum)) for datum in data])

def translate_count_word(num):
    if len(num) != 10:
        return '?'
    special = len(num) != 10 and 'S' or ''
    return 'b' + special + num

class VhdlCountHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Read Count from HX711
        data = self.rfile.readline().strip()

        if data is None:
            return

        print(translate_count(data))

#commands = []
if __name__ ==
