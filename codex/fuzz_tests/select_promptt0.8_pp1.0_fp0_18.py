import select
# Test select.select
print(select.select([], [], []))
 
print(select.select([], [], [1], 1))
 
print(select.select([1], [], []))
 
print(select.select([1], [], [], 1))
 
print(select.select([1,1], [], []))
 
print(select.select([1,1,1], [], []))
 
print(select.select([1,1,1,1,1,1,1], [], []))
 
print(select.select([1,1,1,1,1,1], [], [1]))
 
print(select.select([1,1,1,1,1,1,1], [], []))
 
print(select.select([1,1,1,1,1,1], [], [1]))
 
print(select.select([1,1,1,1,1,1,1], [], []))
 
print(select.select([1,1,1,1,1,1], [],
