import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def load_glove_model(gloveFile):
    print "Loading Glove Model"
    f = codecs.open(gloveFile,'r',encoding='utf-8',errors='replace_with_space')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print "Done.",len(model)," words loaded!"
    return model

def load_glove_model_small(gloveFile):
    print "Loading Glove Model"
    f = codecs.open(gloveFile,'r',encoding='utf-8',errors='replace_with_space')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[
