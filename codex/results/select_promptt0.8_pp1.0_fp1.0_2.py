import select
# Test select.select() function
events = select.select([inFile], [], [], 1)  # if change 1 to 0, it will be a none-blocking mode, means if nothing to read then it will directly skip
if events:
    print(events)
    print(inFile.read(1))
print("after reading")
