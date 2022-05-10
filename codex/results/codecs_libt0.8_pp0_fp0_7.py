import codecs
codecs.register(lambda x: codecs.lookup("utf-8") if x == "cp65001" else None)
import collections
import itertools

def main():
    # for test
    # file_dir = r"F:\ipython\voicetotext\res"
    # file_name = "dan_6.txt"

    # for line
    # file_name = "li_line.txt"
    # file_name = "dan_line.txt"

    # for full
    # file_name = "full_li.txt"
    file_name = "dan_full.txt"

    words = get_special_words(file_name)
    print len(words)
    print words[:100]
    save_words_to_file(words, file_name)
    # save_to_excel(file_name)

def get_special_words(file_name):
    with open(file_name, "r") as f:
        words = []
        for line in f:
            line = line.strip()
           
