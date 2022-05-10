from types import FunctionType
list(FunctionType(de, [1], {})(False,True))
def doo(x): return [x,x]
map(doo,[1,2,3,4,5])

lines = [line for line in open('junkfile') if line.strip() != ""]
lines

[print(num) for num in range(1,100) if num % 3 == 0 or num % 5 == 0]


[(x,y) for x in range(1,10) if x % 2 == 0 for y in range(1,10) if y % 2 == 1]

[air_temp for city, air_temp in cities if city == "Boston"]

#A list comprension use [ ] to create a list straight away all in one go.
