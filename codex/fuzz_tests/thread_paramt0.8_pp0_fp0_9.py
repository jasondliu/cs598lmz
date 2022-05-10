import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from other thread\n')).start()
import spacy
nlp = spacy.load('en')
from spacy.matcher import Matcher
import pandas as pd
matcher = Matcher(nlp.vocab)
from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()
SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "agent", "expl"]
OBJECTS = ["dobj", "dative", "attr", "oprd"]
 
def get_ent_pairs(text):
    ent_pairs = []
    prev_tok_dep = ""
    prev_tok_text = ""
    sub_in = ""
    sub_out = ""
    obj_in = ""
    obj_out = ""
    text = nlp(text)
    for tok in text:
        if tok.dep_ not in ["punct", "cc"]:
            if tok.dep_ in
