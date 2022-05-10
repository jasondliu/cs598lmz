import codecs
codecs.register_error('replace_with_space', replacements.replace_with_space)

#
# This function is called by the multiprocessing module to do the actual work
#
def process_line(line):
    #
    # Replace newlines with spaces and strip whitespace
    #
    line = line.replace('\n',' ').strip()
    #
    # If there is anything left, split it into words and count them
    #
    if len(line) > 0:
        words = line.split()
        for word in words:
            #
            # Decode the word and convert to lower case
            #
            word = word.decode('utf-8', 'replace_with_space').lower()
            #
            # Update the counter for this word
            #
            word_counts[word] += 1

#
# This function is called by the multiprocessing module to do the actual work
#
def process_line_with_lock(line):
    #
    # Replace newlines with spaces and strip whitespace
    #
    line = line.replace('\n','
