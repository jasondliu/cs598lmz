import threading
threading.stack_size(67108864)

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global code
        code = {}

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    current = root
    ans = ""
    for i in s:
        if i == "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            ans += current.data
            current = root
    print ans

ip = raw_input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman
