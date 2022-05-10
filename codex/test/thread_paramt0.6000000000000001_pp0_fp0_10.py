import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

# Load in the data
with open(r'C:\Users\jdavies\Documents\GitHub\learning-python\Data Science\input.txt') as f:
    data = f.read().strip()

# Part 1 Solution
nice_strings = 0
for line in data.split('\n'):
    if len(re.findall('[aeiou]', line)) >= 3 and re.search('(.)\1', line) and not re.search('ab|cd|pq|xy', line):
        nice_strings += 1
print(nice_strings)

# Part 2 Solution
nice_strings = 0
for line in data.split('\n'):
    if re.search('(..).*\1', line) and re.search('(.).\1', line):
        nice_strings += 1
