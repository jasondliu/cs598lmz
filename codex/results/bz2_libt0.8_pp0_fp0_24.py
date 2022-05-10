import bz2
bz2_file = bz2.BZ2File('data/train.ft.txt.bz2')
with open('data/train.ft.txt', 'w') as new_file, bz2_file as file:
    for data in iter(lambda: file.read(100 * 1024), b''):
        new_file.write(data)
bz2_file.close()
# Read the text file, split it by new lines and assign it to a variable.
text = open('data/train.ft.txt').read().split('\n')

# Print out the first and last lines.
text[0], text[-1]

__label__2 Great CD: My lovely Pat has one of the GREAT voices of her generation. I have listened to this CD for YEARS and I still LOVE IT. When I\'m in a good mood it makes me feel better. A bad mood just evaporates like sugar in the rain. This CD just oozes LIFE. _Thank you_ Pat!

__label__1 : I feel so LUCKY to have this CD! It is in the wonderful tradition of Patti Page
