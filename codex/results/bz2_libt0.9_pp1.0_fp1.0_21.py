import bz2
bz2.BZ2File.readline = lambda x: x.readline().decode("utf-8")

from os import path
from keras.preprocessing.text import text_to_word_sequence, Tokenizer

WORDS_FILE = "words"
RATINGS_FILE = "ratings-train"
NUM_WORDS = 7000

words_path = path.join("cache", WORDS_FILE + ".pkl")
ratings_path = path.join("cache", RATINGS_FILE + ".pkl")

if path.exists(wo
