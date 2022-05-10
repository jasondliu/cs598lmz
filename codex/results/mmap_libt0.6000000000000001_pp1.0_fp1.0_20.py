import mmap
import numpy as np
import os
import sys


def load_glove_model(gloveFile):
    print("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print("Done.",len(model)," words loaded!")
    return model

def get_embedding(w, embedding_size, embedding_model):
    embedding = embedding_model[w] if w in embedding_model else embedding_model['unk']
    return embedding

def get_embeddings(words, embedding_size, embedding_model):
    embeddings = []
    for word in words:
        embedding = get_embedding(word, embedding_size, embedding_model)
        embeddings.append(embedding)
    return embeddings


