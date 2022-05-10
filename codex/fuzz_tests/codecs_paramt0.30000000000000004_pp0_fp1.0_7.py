import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    """
    Main function
    """
    # Parse command line arguments
    args = parse_args()

    # Read the input file
    with codecs.open(args.input, 'r', 'utf-8', 'strict') as input_file:
        input_text = input_file.read()

    # Remove all the HTML tags
    input_text = re.sub(r'<[^>]*>', '', input_text)

    # Remove all the non-word characters
    input_text = re.sub(r'\W+', ' ', input_text)

    # Split the text into words
    words = input_text.split()

    # Count the words
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the words by frequency
    sorted_words = sorted(word_count.items(),
