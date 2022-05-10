from _struct import Struct
s = Struct.__new__(Struct)

print s
nums = []
ans = 0
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

with open('input.txt','r') as f:
  for line in f:
    line = line.rstrip()
    pre_letter, num, post_letter = re.split(r'\s+', line)
    nums.append(int(num))

nums = sorted(nums)
#print nums, d

for i in nums:
  if i in d.values():
    ans += i*(10**len(str(i)))

ans += (1 * (10**(len(str(25))+1)))
print ans+1

with open('outp
