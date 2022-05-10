import mmap
import sys

DATA_ROOT = r"../../data/record/"
RESULT_ROOT = r"../../data/results/"
BREAK = "================================="


def create_lizi_data():
    print("reading data for lizi")
    input_file = open(DATA_ROOT + "data.tsv", "r")
    data = input_file.read().replace('\n', BREAK)

    sentences = []
    print("processing data")
    tokenized_data = data.split(BREAK)

    for line in tokenized_data:

        tokens = line.split("\t")
        if len(tokens) > 3:
            sentence = tokens[-2]
            paragraphs = [paragraph.strip() for paragraph in sentence.splitlines()]

            for paragraph in paragraphs:
                if paragraph != "":
                    sentences.append(paragraph)

    print("creating dataset")
    dataset = Dataset()

    # text2paragraph
    text2paragraph = []
    print("add text2paragraph")
    text_id = 0
