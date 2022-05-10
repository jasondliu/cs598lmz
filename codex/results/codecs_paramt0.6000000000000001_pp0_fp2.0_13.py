import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
    file = codecs.open(filename, 'r', 'utf-8')
    lines = file.read().splitlines()
    return lines

def write_file(filename, lines):
    file = codecs.open(filename, 'w', 'utf-8')
    for line in lines:
        file.write(line + '\n')
    file.close()

def remove_word(word, lines):
    result = []
    for line in lines:
        if line == word:
            continue
        result.append(line)
    return result

def remove_words_from_file(filename, words):
    lines = read_file(filename)
    for word in words:
        lines = remove_word(word, lines)
    write_file(filename, lines)

def remove_words_from_files(filenames, words):
    for filename in filenames:
        remove_words_from_file(filename, words)

def
