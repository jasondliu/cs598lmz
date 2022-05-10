import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def main():
    """
    Main function
    """
    # check file path
    if len(sys.argv) != 2:
        print("Usage: python3 {} <file>".format(sys.argv[0]))
        sys.exit(1)

    # get file path
    file_path = sys.argv[1]

    # open file
    f = open(file_path, 'r')

    # loop through file lines
    for line in f:
        # parse line
        line_obj = json.loads(line)

        # get created_at
        created_at = line_obj['created_at']

        # get tweet id
        tweet_id = line_obj['id']

        # get text
        text = line_obj['text']

        # get user id
        user_id = line_obj['user']['id']

        # get user screen name
        user_screen_name = line_obj['
