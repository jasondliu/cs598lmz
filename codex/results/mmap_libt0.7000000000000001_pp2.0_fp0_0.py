import mmap
import sys

def LongestSubstring(arr):
    dict = {}
    maxlength = 0
    start = 0
    for i,char in enumerate(arr):
        if char not in dict.keys():
            dict[char] = i
        else:
            if dict[char] >= start:
                maxlength = max(maxlength,i-start)
                start = dict[char]+1
            dict[char] = i
    return maxlength


def main():
    arr = sys.stdin.readline().strip('\n')
    print(LongestSubstring(arr))

if __name__ == "__main__":
    main()
