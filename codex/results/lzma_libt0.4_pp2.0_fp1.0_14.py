import lzma
lzma.decompress(data)

# In[ ]:


# Part 2

def decompress(data):
    decompressed = []
    i = 0
    while i < len(data):
        if data[i] == '(':
            marker = data[i+1:data.index(')', i)]
            length, repeats = map(int, marker.split('x'))
            decompressed.append(data[i+len(marker)+2:i+len(marker)+2+length] * repeats)
            i += len(marker) + length + 2
        else:
            decompressed.append(data[i])
            i += 1
    return ''.join(decompressed)

print(len(decompress(data)))

# In[ ]:


# Part 2

def decompress2(data):
    decompressed = []
    i = 0
    while i < len(data):
        if data[i] == '(':
            marker = data[i+1:data.index(')', i)]
            length, repeats
