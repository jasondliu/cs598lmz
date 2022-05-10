import threading
threading.currentThread().name

 
#%% 
# (3) Part 1: This gets called a lot so the new Thread class was used instead. 
def pln_builder(title, text, lst):
    # (1) This is a very simple part of speech tagger.  
    # (2) These are all NN/NNS. They can also be VB or VBG.
    # POS = ('N' or 'V') Word = (string)
    # tag and word pairs -> [('N', 'adaptation'), ('N', 'mallards')]
    tag_wrd = nltk.pos_tag(nltk.word_tokenize(text))
    # loop through tagged words
    for item in tag_wrd:
        # check for the desired tags
        if item[1] in ('NN', 'NNS'):
            # check the list of Noun Phrases
            if item[0] not in lst:
                # append noun phrases to this list
                lst.append(item[0])
    # return to calling function
    return (
