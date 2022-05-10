import threading
threading.stack_size(67108864)

def main():
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    sys.stdin = codecs.getreader('utf8')(sys.stdin)

    #Create a dictionary to store the words
    word_dict = {}

    #Read the input
    for line in sys.stdin:
        line = line.strip()
        #Split the line into words
        words = line.split()
        #Iterate through the words and update the dictionary
        for word in words:
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    #Sort the dictionary
    sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1))
    #Print the top 10 words
