import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(['hello', 'world']) + '\n')).start()

# print('hello', 'world')


def checkio(text):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = {}
    for alphabet in alphabets:
        result[alphabet] = 0
    for character in text.lower():
        if character in alphabets:
            result[character] = result[character] + 1
    for key in result:
        print('{0} : {1}'.format(key, result[key]))
    print("")
    return sorted(result, key=lambda x: (-result[x], x))[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
