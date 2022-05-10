import lzma
lzma.open('test.csv.xz').__next__()

# Data Structure

a = ['{a', 'b}', '{c}', '{<c', '>d}', '{e}']
b = ['a', 'b', 'c', 'd', 'e']
i = 0
j = 0
while(i!=len(a) and j!=len(b)):
    if "{" in a[i]:
        print(b[j])
        i += 1
    elif "<" in a[i]:
        j -= 1
        i += 1
    else:
        i += 1
        j += 1

# dict
words = ['ab', 'ac', 'ab', 'ac']
count = {}
for word in words:
    count[word] = 0
for word in words:
    count[word] = count.get(word,0)+1
print(count)

letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)
    if letter == 'b':
        letters
