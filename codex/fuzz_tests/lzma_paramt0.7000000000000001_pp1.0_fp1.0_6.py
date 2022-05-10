from lzma import LZMADecompressor
LZMADecompressor().decompress(bz2.decompress(response.content))

def compare_strings(string1, string2):
    if len(string1) != len(string2): 
        return False
    else:
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
        return True

with open("channel/90052.txt") as out:
    filename = out.readline().rstrip("\n").split(" ")[-1]
    string = ""
    while filename != "comments.txt":
        with open("channel/" + filename) as out:
            string += out.readline().rstrip("\n")
            filename = out.readline().rstrip("\n").split(" ")[-1]
    print(string)
    
with open("channel/90052.txt") as out:
    filename = out.readline().rstrip("\n").split(" ")[-1]
    zip_comment = ""
    while filename != "comments.txt":
        with open("
